"""
程序逻辑配置和第三方平台配置
"""

# Redis配置
REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 5,
}


# 反悔的配置
REWIND_TIMES = 3  # 每天反悔次数
REWIND_TIMEOUT = 60 * 5  # 反悔的超时时间


# 云之讯短信平台配置
YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMS_ARGS = {
    "sid": "2ff56f07e2d002ab9900777dd4b09edf",
    "token": "d763718424035afc347cbd3bba3813a2",
    "appid": "8235102f41ed4603802b05264c59430e",
    "templateid": "503617",
    "param": None,
    "mobile": None,
}


QN_AK = '5UedIsOuzwK10ADuiTKJHfjFXkQukbF8ps9WDEn8'
QN_SK = '_nZH8NNdxGEIt7lvVYLsoAhFODNsgYpTUySn8nx2'
QN_BUCKET_NAME = 'snz'
QN_BASE_URL = 'http://q6cmz3k8e.bkt.clouddn.com'
