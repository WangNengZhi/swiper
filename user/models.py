from django.db import models


class User(models.Model):
    SEX = (
        ('mail', '男性'),
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
    gender = models.CharField(max_length=6, choices=SEX, verbose_name='性别')
    birthday = models.DateField(default='1995-01-01', verbose_name='生日')
    location = models.CharField(max_length=32, choices=LOCATION, verbose_name='常居地')
    avatar = models.ImageField(max_length=256, verbose_name='个人形象')

    class Meta:
        db_table = 'user'
