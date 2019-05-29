
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
'''

      登录相关api、

'''
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

        if(True):
            result['userName'] = userName
            result['password'] = password
            result['isLoginSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)

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

        if(True):
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
        userName = request.POST['userName']
        password = request.POST['password']
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''

        if (True):
            result['userName'] = userName
            result['password'] = password
            result['isResetSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)



'''

      相关api、

'''

