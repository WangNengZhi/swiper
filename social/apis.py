from libs.http import render_json
from social import logics
from user.models import User
from social.models import Friend


def rcmd_users(request):
    """推荐用户接口"""
    users = logics.rcmd(request.uid)
    rcmd_data = [user.to_dict() for user in users]
    return render_json(rcmd_data)


def like(request):
    """右滑喜欢"""
    sid = int(request.POST.get('sid'))
    is_matched = logics.like_someone(request.uid, sid)
    return render_json({'is_matched': is_matched})


def super_like(request):
    """上滑超级喜欢"""
    sid = int(request.POST.get('sid'))
    is_matched = logics.super_like_someone(request.uid, sid)
    return render_json({'is_matched': is_matched})


def dislike(request):
    """左滑不喜欢"""
    sid = int(request.POST.get('sid'))
    logics.dislike_someone(request.uid, sid)

    return render_json()


def rewind(request):
    """反悔操作"""

    logics.rewind_swiper(request.uid)
    return render_json()


def who_like_me(request):
    """查看谁喜欢过自己"""
    users = logics.users_liked_me(request.uid)
    result = [user.to_dict() for user in users]
    return render_json(result)


def friend_list(request):
    """查看自己的好友列表"""
    fid_list = Friend.friend_id_list(request.uid)
    friends = User.objects.filter(id__in=fid_list)
    result = [frd.to_dict() for frd in friends]
    return render_json(result)
