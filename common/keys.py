"""各种缓存的 key"""

VCODE_K = 'Vcode-%s'  # 验证码的 key 拼接手机号

FIRST_RCMD_K = 'FIRST_RCMD_Q-%s'  # 优先推荐队列 拼接uid

REWIND_k = 'Rewind-%s-%s'  # 反悔次数的 key 拼接当天的日期和 uid
