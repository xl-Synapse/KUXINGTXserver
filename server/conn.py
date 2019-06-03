#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core import serializers

from .models import *


def sign_up(name, password, records, treasure):
    """
    注册业务
    :param 用户信息：name、password、records、treasure
    :return: true   false
    """
    # user = cust   omer(name='wo', password='ni', records=0, treasure=0)
    users = customer.objects.filter(name=name, password=password)
    if users:
        return False
    else:
        user = customer(name=name, password=password, records=records, treasure=treasure)
        user.save()
        return True


def sign_in(name, password):
    """
    登陆业务
    :param 用户信息：name、password
    :return: true   false
    """
    user = customer.objects.filter(name=name, password=password)
    if user:
        return True
    else:
        # 用户名或密码错误
        return False


def find_customer(uid):
    """
    内部函数：查找返回customer对象
    :param uid: 用户id
    :return: customer None
    """
    mcustomer = customer.objects.filter(id=uid)
    if mcustomer:
        for m in mcustomer:
            return m
    else:
        return None


def query_info(name, password):
    """
    查询用户信息业务
    :param 用户信息：name、password
    :return: 用户信息的 json 字段
    """
    user = customer.objects.filter(name=name, password=password)
    if user:
        # user = list(user)
        # userinfo = json.dumps(user)
        userinfo = serializers.serialize("json", user)
        print(userinfo)
        return userinfo
    else:
        return None


def modify_info(oname, opassword, nname, npassword):
    """
    修改用户信息
    :param 原用户信息：name、password 新用户信息：name、password
    :return: true   false
    """
    user = customer.objects.filter(name=oname, password=opassword)
    if user:
        user.name = nname
        user.password = npassword
        user.save()
        return True
    else:
        return False


def trends_my_add(uid, date, article):
    """
    添加动态信息
    :param uid: 用户id
    :param date: 产生日期
    :param article: 动态内容
    :return: true   false
    """
    mytrends = trends(uid=uid, date=date, article=article)
    mytrends.save()
    return True


def trends_my_one_quer(uid, date):
    """
    查询返回一个动态
    :param date: 查询日期
    :param uid: 用户id
    :return: 有动态 json 无动态 None
    """
    my_one_trends = trends.objects.filter(uid=uid, date=date)
    if my_one_trends:
        my_one_trends = serializers.serialize("json", my_one_trends)
        return my_one_trends
    else:
        return None


def trends_my_all_quer(uid):
    """
    返回所有动态
    :param uid: 用户id
    :return: 动态信息json / None
    """
    my_all_trends = trends.objects.filter(uid=uid)
    if my_all_trends:
        my_all_trends = serializers.serialize("json", my_all_trends)
        return my_all_trends
    else:
        return None


def trends_other_all_quer(uid):
    """
    返回朋友动态信息
    :param uid: 朋友id
    :return: 动态信息json / None
    """
    return trends_my_all_quer(uid)


def notes_my_add(uid, date, title, article):
    """
    个人记事添加
    :param uid: 个人 id
    :param date: 产生日期
    :param title: 记事标题
    :param article:  记事内容
    :return: 执行结果：true   false
    """
    notes(uid=uid, date=date, title=title, article=article).save()
    return True


def notes_my_one_quer(uid, date):
    """
    返回记事信息
    :param uid: 用户id
    :param date: date
    :return: 记事内容json / None
    """
    my_one_note = notes.objects.filter(uid=uid, date=date)
    if my_one_note.exists:
        my_one_note = serializers.serialize("json", my_one_note)
        return my_one_note
    else:
        return None


def onte_my_all_quer(uid):
    """
    返回所有记事信息
    :param uid: 用户id
    :return: 所有记事 json / None
    """
    my_all_notes = notes.objects.filter(uid=uid)
    if my_all_notes:
        my_all_notes = serializers.serialize("json", my_all_notes)
        return my_all_notes
    else:
        return None


def onte_my_one_del(uid, date):
    """
    删除一个记事
    :param uid: 用户id
    :param date: date
    :return: 执行结果 true  false
    """
    notes.objects.filter(uid=uid, date=date).delete()
    return True


def note_my_all_del(uid):
    """
    删除所有记事
    :param uid: 用户 id
    :return: 执行结果 true false
    """
    notes.objects.filter(uid=uid).delete()
    return True


def relation_add(uid, fid, nick_name, description):
    """
    添加好友关系
    :param uid: 用户id
    :param fid: 好友id
    :param nick_name: 昵称
    :param description: 描述
    :return: true   false
    """
    me = find_customer(uid)
    fr = find_customer(fid)
    if me and fr:
        me_ = relation.objects.filter(uid=me, fid=fr)
        fr_ = relation.objects.filter(uid=fr, fid=me)
        if me_ and fr_:
            relation(uid=me, fid=fr, mconfirm=1, fconfirm=1, nick_name=nick_name, description=description).save()
            relation(uid=fr, fid=me, mconfirm=0, fconfirm=1).save()
            return True
        else:
            # 表示关系已存在
            return True
    else:
        return False


def relation_confirm(uid, fid, nick_name, description):
    """
    朋友好友确认
    :param uid: 用户 id
    :param fid: 好友 fid
    :param nick_name: 昵称
    :param description: 描述
    :return: true false
    """
    me = find_customer(uid)
    fr = find_customer(fid)
    mrelation = relation.objects.filter(uid=me, fid=fr)
    if mrelation:
        mrelation.mconfirm = 1
        frelation = relation.objects.filter(uid=fr, fid=me)
        if frelation:
            mrelation.nick_name = nick_name
            mrelation.description = description
            frelation.fconfirm = 1
            mrelation.save()
            frelation.save()
            return True
        else:
            mrelation.mconfirm = 0
            return False
    else:
        return False


def relation_del(uid, fid):
    """
    删除好友关系
    :param uid: 用户id
    :param fid: 好友id
    :return: true    false
    """
    relation.objects.filter(uid=uid, fid=fid).delete()
    return True


def relation_my_all_qur(uid):
    """
    查询所有好友信息
    :param uid: 用户id
    :return: 好友关系json 包含内容查看 relation表列字段
    """
    my_relations = relation.objects.filter(uid=uid)
    if my_relations.exists:
        my_relations = serializers.serialize("json", my_relations)
        return my_relations
    else:
        return False


def relation_my_one_qur(uid, fid):
    """
    查找好友关系
    :param uid: 用户id
    :param fid: 好友id
    :return:
    """
    my_relations = relation.objects.filter(uid=uid, fid=fid)
    if my_relations.exists:
        my_relations = serializers.serialize("json", my_relations)
        return my_relations
    else:
        return None
