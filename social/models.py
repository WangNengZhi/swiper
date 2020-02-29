from django.db import models


class Swiped(models.Model):
    """滑动记录"""
    STYPE = (
        ('like', '上滑：喜欢'),
        ('superlike', '上滑：超级喜欢'),
        ('dislike', '左滑：不喜欢'),
    )
    uid = models.IntegerField(verbose_name='滑动者的ID')
    sid = models.IntegerField(verbose_name='被滑动着的ID')
    stype = models.CharField(max_length=16, choices=STYPE, verbose_name='滑动类型')
    time = models.DateTimeField(auto_now_add=True, verbose_name='滑动时间')

    class Meta:
        db_table = 'swiped'

    @classmethod
    def is_liked(cls, uid, sid):
        """检查是否喜欢过对方"""
        return cls.objects.filter(uid=uid, sid=sid, stype__in=['like', 'superlike']).exists()


class Friend(models.Model):
    """好友关系"""
    uid1 = models.IntegerField(verbose_name='好友ID')
    uid2 = models.IntegerField(verbose_name='好友ID')

    class Meta:
        db_table = 'friend'
        unique_together = [['uid1', 'uid2']]

    @classmethod
    def make_friend(cls, uid1, uid2):
        """创建好友关系"""
        uid1, uid2 = (uid2, uid1) if uid1 > uid2 else (uid1, uid2)
        cls.objects.create(uid1=uid1, uid2=uid2)
