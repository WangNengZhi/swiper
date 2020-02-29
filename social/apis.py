from libs.http import render_json
from social import logics


def rcmd_users(request):
    """推荐用户接口"""
    users = logics.rcmd(request.uid)
    rcmd_data = [user.to_dict() for user in users]
    return render_json(rcmd_data)


def like(request):
    """右滑喜欢"""
    return render_json()


def super_like(request):
    """上滑超级喜欢"""
    return render_json()


def dislike(request):
    """左滑不喜欢"""
    return render_json()


def rewind(request):
    return render_json()


def who_like_me(request):
    return render_json()


def friend_list(request):
    return render_json()
