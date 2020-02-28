import random
import os

import requests
from django.core.cache import cache

from swiper import config
from user.models import User
from libs.qn_clound import upload_to_qiniu
from tasks import celery_app


def gen_rand_code(length=6):
    """长生指定长度的随即码"""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])


def send_vcode(mobile):
    """发送短信验证码"""
    vcode = gen_rand_code()  # 产生验证码
    cache.set('Vcode-%s' % mobile, vcode, 180)  # 将验证码写入缓存,保存3分钟
    print('验证码:', vcode)

    args = config.YZX_SMS_ARGS.copy()  # 复制前拷贝全局配置
    args['param'] = vcode
    args['mobile'] = mobile

    response = requests.post(config.YZX_SMS_API, config.YZX_SMS_ARGS)  # 调用第三方接口发送验证码
    if response.status_code == 200:
        result = response.json()
        if result['msg'] == 'OK':
            # cache.set(key, vcode, 180)  # 将验证码写入缓存,保存3分钟
            return True
    return False


def save_avatar(uid, avatar_file):
    """将个人形象保存到本地"""
    filename = 'Avatar-%s' % uid
    filepath = '/tmp/%s' % filename
    with open(filepath, 'wb') as fp:
        for chunk in avatar_file.chunks():
            fp.write(chunk)
    return filename, filepath


@celery_app.task
def upload_avatar(uid, avatar_file):
    filename, filepath = save_avatar(uid, avatar_file)  # 文件保存到本地
    avatar_url = upload_to_qiniu(filename, filepath)  # 文件上传到其牛云
    User.objects.filter(id=uid).update(avatar=avatar_url)  # 保存URL
    os.remove(filepath)  # 删除本零时文件
