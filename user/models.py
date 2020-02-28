from django.db import models


class User(models.Model):
    SEX = (
        ('male', '男性'),
        ('female', '女性')
    )
    LOCATION = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('广州', '广州'),
        ('深圳', '深圳'),
        ('杭州', '杭州'),
    )
    phonenum = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=32, verbose_name='昵称')
    gender = models.CharField(max_length=6, choices=SEX, default='male', verbose_name='性别')
    birthday = models.DateField(default='1995-01-01', verbose_name='生日')
    location = models.CharField(max_length=32, choices=LOCATION, default='上海', verbose_name='常居地')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')

    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile

    class Meta:
        db_table = 'user'

    def to_dict(self):
        return {
            'id': self.id,
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'gender': self.gender,
            'birthday': str(self.birthday),
            'location': self.location,
            'avatar': self.avatar,
        }


class Profile(models.Model):
    """个人资料"""
    dating_sex = models.CharField(max_length=6, choices=User.SEX, default='male', verbose_name='目标性别')
    dating_location = models.CharField(max_length=32, choices=User.LOCATION, default='上海', verbose_name='目标城市')
    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50, verbose_name='最大交友年龄')
    vibration = models.BooleanField(default=True, verbose_name='开启振动')
    only_matche = models.BooleanField(default=True, verbose_name='不让未匹配的人查看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')

    class Meta:
        db_table = 'profile'

    def to_dict(self):
        return {
            'id': self.id,
            'dating_sex': self.dating_sex,
            'dating_location': self.dating_location,
            'min_distance': self.min_distance,
            'max_distance': self.max_distance,
            'min_dating_age': self.min_dating_age,
            'max_dating_age': self.max_dating_age,
            'vibration': self.vibration,
            'only_matche': self.only_matche,
            'auto_play': self.auto_play,
        }
