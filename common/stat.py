"""
程序状态玛
"""

OK = 0


class LogicError(Exception):
    code = None
    data = None

    def __init__(self, data=None):
        self.data = data or self.__class__.__name__


def gen_logic_err(name, code):
    """封装一个逻辑异常"""
    return type(name, (LogicError,), {'code': code})


SendSmsErr = gen_logic_err('SendSmsErr', 1000)  # 发送短信异常

VcodeErr = gen_logic_err('VcodeErr', 1001)  # 状态玛异常

LoginRequired = gen_logic_err('LoginRequired', 1002)  # 用户未等登陆

UserFormErr = gen_logic_err('User_Form_Err', 1003)  # 用户表单错误

ProfileFormErr = gen_logic_err('Profile_Form_Err', 1004)  # 资料表单错误

StypeErr = gen_logic_err('StypeErr', 1005)  # 滑动类型错误

ReswipeErr = gen_logic_err('ReswipeErr', 1006)  # 重复滑动一个人

RewindLimit = gen_logic_err('RewindLimit', 1007)  # 反悔次数达到限制

RewindTimeout = gen_logic_err('RewindTimeout', 1008)  # 反悔超时
