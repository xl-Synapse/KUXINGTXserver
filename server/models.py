# coding=utf-8

from django.db import models


class customer(models.Model):
    """ customer类
    information：
        数据库server_customer关联映射

    Attributes：
        id: 用户信息主键
        name: 用户 name
        password：用户 password
        records：用户积分
        treasure：用户财富
    """

    id = models.AutoField("id", primary_key=True)
    name = models.CharField("姓名", max_length=12, null=False)
    password = models.CharField("密码", max_length=12, null=False)
    records = models.SmallIntegerField("积分", null=False)
    treasure = models.SmallIntegerField("财富", null=False)


class notes(models.Model):
    """ notes类
    information：
        关联映射数据库server_notes表

    Attributes：
        id: 表格主键
        uid: 用户关联外键
        date: note产生日期
        title: 记事标题
        article: 记事内容

    """
    id = models.AutoField("id", primary_key=True)
    uid = models.ForeignKey(to="customer", to_field="id", on_delete='CASCADE')
    date = models.DateTimeField("日期")
    title = models.CharField("标题", max_length=12, null=False)
    article = models.TextField("内容", null=False)


class trends(models.Model):
    """ trends类
    information：
        关联映射 server_trends表格
    Attributes：
        id: 表格主键
        uid: 用户关联外键
        date: 动态产生日期
        article: 动态内容
    """
    id = models.AutoField("id", primary_key=True)
    uid = models.ForeignKey(to="customer", to_field="id", on_delete='CASCADE')
    date = models.DateTimeField("日期")
    article = models.TextField("内容", null=False)


class relation(models.Model):
    """ relation类
    information：
        关联映射 server_relation表格
    attributes：
        id: 表格主键
        uid: 用户id
        fid: 好友id
        nick_name: 昵称
        discription: 描述
    """
    id = models.AutoField("id", primary_key=True)
    uid = models.ForeignKey(to='customer', to_field='id', related_name='uid', on_delete='CASCADE', primary_key=False)
    fid = models.ForeignKey(to='customer', to_field='id', related_name='fid', on_delete='CASCADE', primary_key=False)
    mconfirm = models.IntegerField("m确认", null=False)
    fconfirm = models.IntegerField("f确认", null=False)
    nick_name = models.CharField("昵称", max_length=12, null=False)
    description = models.CharField("描述", max_length=24, null=True)
