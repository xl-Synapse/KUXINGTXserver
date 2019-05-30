# coding=utf-8
from django.http import JsonResponse
from django.shortcuts import render
from server.conn import *

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
        if (sign_in(userName,password) == True):
            result['userName'] = userName
            result['password'] = password
            result['isLoginSuccess'] = True
            print("用户:"+userName+" 密码:"+password+" 登录成功！")
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
        if (sign_up(userName, password, 0, 0) == False):
            result['userName'] = userName
            result['password'] = password
            result['isRegisterSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)


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

        if (modify_info(ouserName, opassword, nuserName, npassword) == True):
            result['nuserName'] = userName
            result['npassword'] = password
            result['isResetSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)


'''

      相关api、

'''
