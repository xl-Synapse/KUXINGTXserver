# coding=utf-8
from django.http import JsonResponse
from server.conn import *
import json
# Create your views here.
'''

      登录相关api、

'''
'''                                                                               登录相关的未测试完成'''


def loginPost(request):
    result = {
        'isLoginSuccess': False
    }
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''

        if sign_in(userName, password):
            result['userName'] = userName
            result['password'] = password
            result['isLoginSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)


'''                                                                                       '''


def registerPost(request):
    result = {
        'isRegisterSuccess': False
    }
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''
        '''注册账户 '''
        if sign_up(userName, password, 0, 0):
            result['userName'] = userName
            result['password'] = password
            result['isRegisterSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)

'''尚未实现'''
def resetPassword(request):
    result = {
        'isResetSuccess': False
    }
    if request.method == 'POST':
        ouserName = request.POST['ouserName']
        opassword = request.POST['opassword']
        nuserName = request.POST['nuserName']
        npassword = request.POST['npassword']
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''

        if modify_info(ouserName, opassword, nuserName, npassword):
            # 涛涛更改过变量
            result['nuserName'] = nuserName
            result['npassword'] = npassword
            result['isResetSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)


'''

      相关api、

'''


def query_infoPost(request):
    result = {
        'isQuery_infoSuccess': False
    }
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        print("用户名:"+userName+" 检索用户信息")
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''
        user = query_info(userName,password)
        if user!=None:
            preparedJson=json.loads(user)
            preparedUser=preparedJson[0]["fields"]
            result['userName'] = preparedUser["name"]
            result['password'] = preparedUser["password"]
            result['records'] = preparedUser["records"]
            result['treasure'] = preparedUser["treasure"]
            print("返回信息:\n" +
                  "userName " +  str(result['userName'])+"\n"+
                  "password " + str(result['password']) + "\n" +
                  "records " + str(result['records']) + "\n" +
                  "treasure " + str(result['treasure']) + "\n"
                  )
            # result['Id'] = preparedUser["id"]
            result['isQuery_infoSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)


def modify_infoPost(request):
    """
    修改用户信息
    :param 原用户信息：name、password 新用户信息：name、password
    :return: true   false
    """
    result = {
        'isModify_infoSuccess': False
    }
    if request.method == 'POST':
        ouserName = request.POST['ouserName']
        opassword = request.POST['opassword']
        nuserName = request.POST['nuserName']
        npassword = request.POST['npassword']
        print("用户名:" + ouserName + " 修改用户信息")
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''
        user = modify_info(ouserName, opassword, nuserName, npassword)
        if user :
            result['ouserName'] = ouserName
            result['opassword'] = opassword
            result['nuserName'] = nuserName
            result['npassword'] = npassword
            print("返回信息:\n" +
                  "ouserName " + ouserName+ "\n"+
                  "opassword " + opassword + "\n" +
                  "nuserName " + nuserName + "\n" +
                  "npassword " + npassword + "\n" +
                  "isModify_infoSuccess " + str(True) + "\n"
                  )
            result['isModify_infoSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)


def relation_addPost(request):
    """
    添加好友关系
    :param uid: 用户id
    :param fid: 好友id
    :param nick_name: 昵称
    :param description: 描述
    :return: true   false
    """

    result = {
        'isRelation_addSuccess': False
    }
    if request.method == 'POST':
        uid = request.POST['uid']
        fid = request.POST['fid']
        nick_name = request.POST['nick_name']
        description = request.POST['description']
        print("用户名:" + uid + " 添加好友")
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''
        user = relation_add(uid, fid, nick_name, description)
        if user:
            result['uid'] = uid
            result['fid'] = fid
            result['nick_name'] = nick_name
            result['description'] = description
            print("返回信息:\n" +
                  "ouserName " + ouserName+ "\n"+
                  "opassword " + opassword + "\n" +
                  "nuserName " + nuserName + "\n" +
                  "npassword " + npassword + "\n" +
                  "isRelation_addSuccess " + str(True) + "\n"
                  )
            result['isRelation_addSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)

