# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-02-23 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(max_length=15, unique=True, verbose_name='手机号')),
                ('nickname', models.CharField(max_length=32, verbose_name='昵称')),
                ('gender', models.CharField(choices=[('male', '男性'), ('female', '女性')], default='male', max_length=6, verbose_name='性别')),
                ('birthday', models.DateField(default='1995-01-01', verbose_name='生日')),
                ('location', models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('广州', '广州'), ('深圳', '深圳'), ('杭州', '杭州')], default='上海', max_length=32, verbose_name='常居地')),
                ('avatar', models.CharField(max_length=256, verbose_name='个人形象')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
