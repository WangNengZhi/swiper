from json import dumps

from django.conf import settings
from django.http import HttpResponse


def render_json(data=None, code=0):
    """渲染json返回值"""
    result = {
        'data': data,
        'code': code,
    }

    if settings.DEBUG:
        json_result = dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_result = dumps(result, ensure_ascii=False, separators=(',', ':'))

    return HttpResponse(json_result)
