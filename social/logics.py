import datetime

from user.models import User
from user.models import Profile
from social.models import Swiped
from social.models import Friend


def rcmd(uid):
    """用户推荐"""
    profile, _ = Profile.objects.get_or_create(id=uid)  # 获取用户的交友资料

    today = datetime.datetime.today()
    earliest_birthday = today - datetime.timedelta(profile.max_dating_age * 365)  # 最早出生
    latest_birthday = today - datetime.timedelta(profile.min_dating_age * 36)  # 最晚出生日期

    # 取出已经划过的人的ID
    sid_list = Swiped.objects.filter(uid=uid).values_list('sid', flat=True)

    # 取出需要的用户同时排除已经滑过的用户
    users = User.objects.filter(
        gender=profile.dating_sex,
        location=profile.dating_location,
        birthday__gte=earliest_birthday,
        birthday__lte=latest_birthday,
    ).exclude(id__in=sid_list)[:20]
    return users


def like_someone(uid, sid):
    """喜欢某人"""
    # 添加一条滑动记录
    Swiped.objects.create(uid=uid, sid=sid, stype='like')
    # 检查对方有没有右滑或者上滑过字节
    if Swiped.is_liked(sid, uid):
        # 如果对方有喜欢过自己,匹配成好友
        Friend.make_friend(uid, sid)
        return True
    else:
        return False
