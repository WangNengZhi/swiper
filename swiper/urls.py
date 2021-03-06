"""swiper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from user import apis as user_api
from social import apis as social_api


urlpatterns = [
    # 用户模块接口
    url(r'^api/user/get_vcode', user_api.get_vcode),
    url(r'^api/user/submit_vcode', user_api.submit_vcode),
    url(r'^api/user/get_profile', user_api.get_profile),
    url(r'^api/user/set_profile', user_api.set_profile),
    url(r'^api/user/upload_avatar', user_api.upload_avatar),

    # 社交模块接口
    url(r'^apis/social/rcmd_users', social_api.rcmd_users),
    url(r'^apis/social/like', social_api.like),
    url(r'^apis/social/superlike', social_api.super_like),
    url(r'^apis/social/dislike', social_api.dislike),
    url(r'^apis/social/rewind', social_api.rewind),
    url(r'^apis/social/who_like_me', social_api.who_like_me),
    url(r'^apis/social/friend_list', social_api.friend_list),
]
