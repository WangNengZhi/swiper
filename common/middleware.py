from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from common import stat


class AuthMiddleware(MiddlewareMixin):
    """用户登陆验证"""

    path_white_list = [
        '/api/user/get_vcode',
        '/api/user/submit_vcode',
    ]

    def process_request(self, request):
        # 检查但前路径是否在白名单中
        if request.path not in self.path_white_list:
            uid = request.session.get('uid')
            if not uid:
                return JsonResponse({'code': stat.LOGIN_REQUIRED, 'data': None})
            else:
                request.uid = uid
