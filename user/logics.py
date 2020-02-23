import random

import requests

from swiper import config


def gen_rand_code(length=6):
    """长生指定长度的随即码"""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])


def send_vcode(mobile):
    """发送短信验证码"""
    vcode = gen_rand_code()  # 产生验证码
    print('验证码:', vcode)

    args = config.YZX_SMS_ARGS.copy()  # 复制前拷贝全局配置
    args['param'] = vcode
    args['mobile'] = mobile

    response = requests.post(config.YZX_SMS_API, config.YZX_SMS_ARGS)  # 调用第三方接口发送验证码
    if response.status_code == 200:
        result = response.json()
        if result['msg'] == 'OK':
            return True
    return False
