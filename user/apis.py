from django.core.cache import cache

from user import logics
from common import stat
from common import keys
from user.models import User
from user.models import Profile
from user.forms import UserForm
from user.forms import ProfileForm
from libs.http import render_json


def get_vcode(request):
    """获取短信验证码"""
    phonenum = request.GET.get('phonenum')
    status = logics.send_vcode(phonenum)
    if status:
        return render_json()
    else:
        raise stat.SendSmsErr


def submit_vcode(request):
    """通过验证码登陆, 注册"""
    vcode = request.POST.get('vcode')
    phonenum = request.POST.get('phonenum')

    cache_vcode = cache.get(keys.VCODE_K % phonenum)  # 取出缓存的验证码

    # 检查验证码是否正确
    if vcode and vcode == cache_vcode:
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum)  # 创建用户

        # 执行登陆过程
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    else:
        raise stat.VcodeErr


def get_profile(request):
    """获取个人资料"""
    profile, _ = Profile.objects.get_or_create(id=request.uid)

    return render_json(profile.to_dict())


def set_profile(request):
    """修改个人资料"""
    user_from = UserForm(request.POST)
    profile_from = ProfileForm(request.POST)

    # 检查数据有效性
    if not user_from.is_valid():
        raise stat.UserFormErr(user_from.errors)

    if not profile_from.is_valid():
        raise stat.ProfileFormErr(profile_from.errors)

    data = {}
    data.update(user_from.cleaned_data)
    data.update(profile_from.cleaned_data)
    data['birthday'] = str(data['birthday'])

    # 保存数据
    User.objects.filter(id=request.uid).update(**user_from.cleaned_data)
    Profile.objects.filter(id=request.uid).update(**profile_from.cleaned_data)

    return render_json()


def upload_avatar(request):
    """
    头像上传

    1.保存到本地
    2.上传到七牛云
    3.保存URL
    4.删除本地文件
    """
    avatar_file = request.FILES.get('avatar')
    logics.upload_avatar.delay(request.uid, avatar_file)

    return render_json()
