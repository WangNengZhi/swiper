from django.http import JsonResponse

from user import logics
from common import stat


def get_vcode(request):
    """获取短信验证码"""
    phonenum = request.GET.get('phonenum')
    status = logics.send_vcode(phonenum)
    if status:
        return JsonResponse({'code': stat.OK, 'data': None})
    else:
        return JsonResponse({'code': stat.VCODE_ERR, 'data': None})


def submit_vcode(request):
    """通过验证码登陆, 注册"""
    pass


def set_profile(request):
    """修改个人资料"""
    pass


def upload_avatar(request):
    """头像上传"""
    pass
