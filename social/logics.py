import datetime

from common import keys
from libs.cache import rds
from user.models import User
from user.models import Profile
from social.models import Swiped
from social.models import Friend


def first_rcmd(uid):
    """从Redis的优秀推荐列表中获取要推荐的用户"""
    uid_list = rds.lrange(keys.FIRST_RCMD_K % uid, 0, 20)
    uid_list = [int(uid) for uid in uid_list]  # 将uid_list中的bytes强转成int
    return User.objects.filter(id__in=uid_list)


def rcmd_from_db(uid, num, exclude__ids=()):
    """从数据库获取要推荐的用户"""
    profile, _ = Profile.objects.get_or_create(id=uid)  # 获取用户的交友资料

    today = datetime.datetime.today()
    earliest_birthday = today - datetime.timedelta(profile.max_dating_age * 365)  # 最早出生
    latest_birthday = today - datetime.timedelta(profile.min_dating_age * 36)  # 最晚出生日期

    # 取出已经划过的人的ID
    sid_list = Swiped.objects.filter(uid=uid).values_list('sid', flat=True)
    exclude__ids = list(exclude__ids) + list(sid_list)

    # 取出需要的用户同时排除已经滑过的用户
    users = User.objects.filter(
        gender=profile.dating_sex,
        location=profile.dating_location,
        birthday__gte=earliest_birthday,
        birthday__lte=latest_birthday,
    ).exclude(id__in=exclude__ids)[:num]

    return users


def rcmd(uid):
    """推荐接口"""
    first_users = first_rcmd(uid)  # 首先从优先推荐队列中取出用户
    count = 20 - len(first_users)  # 计算需要从数据库中取出的用户数量
    first_user_id_list = [u.id for u in first_users]
    db_users = rcmd_from_db(uid, count)  # 从数据苦衷取出用户
    return list(first_users) + list(db_users)


def like_someone(uid, sid):
    """喜欢某人"""
    # 添加一条滑动记录
    Swiped.objects.create(uid=uid, sid=sid, stype='like')

    # 将sid从优先队列中删除
    rds.lrem(keys.FIRST_RCMD_K % uid, 0, sid)

    # 检查对方有没有右滑或者上滑过字节
    if Swiped.is_liked(sid, uid):
        # 如果对方有喜欢过自己,匹配成好友
        Friend.make_friend(uid, sid)
        return True
    else:
        return False


def super_like_someone(uid, sid):
    """超级喜欢"""
    # 添加滑动记录
    Swiped.objects.create(uid=uid, sid=sid, stype='superlike')

    # 将sid从优先队列中删除
    rds.lrem(keys.FIRST_RCMD_K % uid, 0, sid)

    liked_me = Swiped.is_liked(sid, uid)
    if liked_me:
        Friend.make_friend(uid, sid)
        return True
    elif not liked_me:
        return False
    else:
        # 对方没有滑动过自己，将自己的uid添加到对方的 “优先推荐队列”
        rds.rpush(keys.FIRST_RCMD_K % sid, uid)
        return False
