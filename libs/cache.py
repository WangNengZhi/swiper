from pickle import dumps, loads, HIGHEST_PROTOCOL, UnpicklingError

from redis import Redis as _Redis

from swiper.config import REDIS


class Redis(_Redis):
    def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        """带序列化处理的set方法"""
        picked_value = dumps(value, HIGHEST_PROTOCOL)
        super().set(name, picked_value, ex, px, nx, xx)

    def get(self, name, default=None):
        """带反序列化处理默认值的get方法"""
        picked_value = super().get(name)
        if not picked_value:
            return default
        else:
            try:
                return loads(picked_value)
            except UnpicklingError:
                return picked_value


rds = Redis(**REDIS)
