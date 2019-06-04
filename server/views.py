# coding=utf-8
import json
import time
import os
import re

from django.http import JsonResponse

from server.conn import *

pathHead = "E:\work\Python\KUXINGTXserver/trendsInfo"
httpServerHead="http://192.168.1.199:8001"+"/"
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
        user = sign_in(userName, password)

        print("用户名:" + userName + " 请求登录")
        print("返回信息:\n" +
              "userName " + userName + "\n" +
              "password " + password + "\n" +
              "id " + str(user.id) + "\n"
              )
        if user:
            result['id']=user.id
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
        print("用户名:" + userName + " 检索用户信息")
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''
        user = query_info(userName, password)
        if None != user:
            preparedJson = json.loads(user)
            preparedUser = preparedJson[0]["fields"]
            result['userName'] = preparedUser["name"]
            result['password'] = preparedUser["password"]
            result['records'] = preparedUser["records"]
            result['treasure'] = preparedUser["treasure"]
            print("返回信息:\n" +
                  "userName " + str(result['userName']) + "\n" +
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
        if user:
            result['ouserName'] = ouserName
            result['opassword'] = opassword
            result['nuserName'] = nuserName
            result['npassword'] = npassword
            print("返回信息:\n" +
                  "ouserName " + ouserName + "\n" +
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
    :param: request
    :return: true   false
    """

    result = {
        'isRelation_addSuccess': False
    }
    if request.method == 'POST':
        uid = int(request.POST['uid'])
        fid = int(request.POST['fid'])
        nick_name = request.POST['nick_name']
        description = request.POST['description']
        print("用户名:" + str(uid) + " 添加好友")
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
                  "uid " + str(uid) + "\n" +
                  "fid " + str(fid) + "\n" +
                  "nick_name " + nick_name + "\n" +
                  "description " + description + "\n" +
                  "isRelation_addSuccess " + str(True) + "\n"
                  )
            result['isRelation_addSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)


def relation_confirmPost(request):
    """
    添加好友关系
    :param: request
    :return: true   false
    """

    result = {
        'isRelation_confirmSuccess': False
    }
    if request.method == 'POST':
        uid = int(request.POST['uid'])
        fid = int(request.POST['fid'])
        nick_name = request.POST['nick_name']
        description = request.POST['description']
        print("用户名:" + str(uid) + " 确认好友请求")
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''
        user = relation_confirm(uid, fid, nick_name, description)
        if user:
            result['uid'] = uid
            result['fid'] = fid
            result['nick_name'] = nick_name
            result['description'] = description
            print("返回信息:\n" +
                  "uid " + str(uid) + "\n" +
                  "fid " + str(fid) + "\n" +
                  "nick_name " + nick_name + "\n" +
                  "description " + description + "\n" +
                  "isRelation_confirmSuccess " + str(True) + "\n"
                  )
            result['isRelation_confirmSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)


def relation_confirmPost(request):
    """
    添加好友关系
    :param: request
    :return: true   false
    """

    result = {
        'isRelation_confirmSuccess': False
    }
    if request.method == 'POST':
        uid = int(request.POST['uid'])
        fid = int(request.POST['fid'])
        nick_name = request.POST['nick_name']
        description = request.POST['description']
        print("用户名:" + str(uid) + " 确认好友请求")
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''
        user = relation_confirm(uid, fid, nick_name, description)
        if user:
            result['uid'] = uid
            result['fid'] = fid
            result['nick_name'] = nick_name
            result['description'] = description
            print("返回信息:\n" +
                  "uid " + str(uid) + "\n" +
                  "fid " + str(fid) + "\n" +
                  "nick_name " + nick_name + "\n" +
                  "description " + description + "\n" +
                  "isRelation_confirmSuccess " + str(True) + "\n"
                  )
            result['isRelation_confirmSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)

def relation_delPost(request):
    """
    删除好友关系
    :param: request
    :return: true   false
    """

    result = {
        'isRelation_delSuccess': False
    }
    if request.method == 'POST':
        uid = int(request.POST['uid'])
        fid = int(request.POST['fid'])
        print("用户名:" + str(uid) + " 删除好友请求")
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''
        user = relation_del(uid, fid)
        if user:
            result['uid'] = uid
            result['fid'] = fid
            print("返回信息:\n" +
                  "uid " + str(uid) + "\n" +
                  "fid " + str(fid) + "\n" +
                  "isRelation_delSuccess " + str(True) + "\n"
                  )
            result['isRelation_delSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)


def relation_my_all_qurPost(request):
    """
    我的所有请求
    :param: request
    :return: true   false
    """

    result = {
        'isRelation_my_all_qurSuccess': False
    }
    if request.method == 'POST':
        uid = int(request.POST['uid'])
        print("用户名:" + str(uid) + " 查询所有好友请求")
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''
        user = relation_my_all_qur(uid)
        if user:
            result['uid'] = uid
            resultContent=[]
            preparedJson = json.loads(user)
            for m in preparedJson:
                resultContent.append(m["fields"])
                print(m)
                preparedContent = resultContent
            print("返回信息:\n" +
                  "uid " + str(uid) + "\n" +
                  "resultContent " + str(preparedContent) + "\n" +
                  "isRelation_my_all_qurSuccess " + str(True) + "\n"
                  )

            result['resultContent']=preparedContent
            result['isRelation_my_all_qurSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)

def relation_my_one_qurPost(request):
    """
    我的单一好友请求
    :param: request
    :return: true   false
    """

    result = {
        'isRelation_my_one_qurSuccess': False
    }
    if request.method == 'POST':
        uid = int(request.POST['uid'])
        fid = int(request.POST['fid'])
        print("用户名:" + str(uid) + " 查询所有好友请求")
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''
        user = relation_my_one_qur(uid,fid)
        if user:
            result['uid'] = uid
            result['fid'] = fid
            resultContent=[]
            preparedJson = json.loads(user)
            for m in preparedJson:
                resultContent.append(m["fields"])
                print(m)
                preparedContent = resultContent
            print("返回信息:\n" +
                  "uid " + str(uid) + "\n" +
                  "resultContent " + str(preparedContent) + "\n" +
                  "isRelation_my_one_qurSuccess " + str(True) + "\n"
                  )

            result['resultContent']=preparedContent
            result['isRelation_my_one_qurSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)

def trends_my_addPost(request):

    """
    添加动态信息
    :param uid: 用户id
    :param date: 产生日期  规定日期格式为（%Y-%m-%d %H:%M:%S）
    :param article: 动态内容
    :return: true   false
    """

    result = {
        'isTrends_my_addSuccess': False
    }

    img=[]
    if request.method == 'POST':
        uid = int(request.POST['uid'])
        date = request.POST['date']
        content= request.POST['content']
        imgNumber=int(request.POST['imgNumber'])
        for i in range(imgNumber):
            img.append(request.FILES.get("img"+str(i)))
        print("用户名:" + str(uid) + " 添加动态信息")
        # 调用数据库的接口、
        '''
        这里需要接入数据库接口
        '''


        user = trends_my_add(uid,date,content)

        if user:
            print("数据库操作成功，建立文件结构")
            #os.mkdir(pathHead+"/trendsInfo")
            trendInfo = json.loads(trends_my_one_quer(uid,date))
            trendId = -1

            print(str(img[0]))
            for m in trendInfo:
                trendId = m['pk']
            os.mkdir(pathHead+"/"+str(trendId))             #建立一个关联trend的目录

            # 将content通过正则修改其url
            oldUrl = getSourceUrl(content)
            tmpContent = content
            for i in range(0, len(oldUrl)):
                tmpContent = tmpContent.replace(oldUrl[i], httpServerHead+str(trendId)+"/"+str(i))
                print(tmpContent)
            content = tmpContent
            trends_change_content(trendId, content)         #修改数据库表

            for i in range(imgNumber):                     #图片写入服务器目录
                file_name= str(img[i])
                file_type=getImgType(file_name)
                file_final_name=pathHead+"/"+str(trendId)+"/"+str(i)+file_type
                destination = open(file_final_name, 'wb+')  # 打开特定的文件进行二进制的写操作
                for chunk in img[i].chunks():  # 分块写入文件
                    destination.write(chunk)
                destination.close()



                # file_object = open(file_final_name,"wb+", buffering=1)
                # file_object.write(img[i])
                # file_object.close()

            result['isTrends_my_addSuccess'] = True
            return JsonResponse(result)
    return JsonResponse(result)


def getImgType(img_name):
    pattern="\.(png|bmp|jpg|jpeg)"
    string =img_name
    result=re.search(pattern,string,flags=0)
    if result:
        return result.group()
    return None

def getSourceUrl(content):
    pattern = "<img src=\"(.*?)\."
    string = content
    result = re.findall(pattern, string, flags=0)

    if result:
        return result
    return None

def trends_my_all_querPost(request):
    """
       我的所有请求
       :param: request
       uid
       :return: true   false
       """

    result = {
        'isTrends_my_all_querSuccess': False,
    }
    result['resultContent'] = None

    if request.method == 'POST':
        uid = int(request.POST['uid'])

        fid = relation_my_all_qur(uid)

        resultContent = []
        print("用户名:" + str(uid) + " 查询所有好友动态")

        user = trends_my_all_quer(uid)
        print(user)
        if user:
            preparedJson = json.loads(user)
            for m in preparedJson:
                resultContent.append(m["fields"])
                print(m)


        preparedFid=json.loads(fid)
        for m in preparedFid:
            user = trends_my_all_quer(m['fields']['fid'])
            print(user)
            if user:

                preparedJson = json.loads(user)
                for m in preparedJson:
                    resultContent.append(m["fields"])
                    print(m)

        result['resultContent'] = resultContent
        result['isTrends_my_all_querSuccess'] = True
        return JsonResponse(result)
    # """
    #    我的所有请求
    #    :param: request
    #    :return: true   false
    #    """
    #
    # result = {
    #     'isTrends_my_all_querSuccess': False,
    # }
    # result['resultContent'] = None
    #
    # if request.method == 'POST':
    #     uid = int(request.POST['uid'])
    #     print("用户名:" + str(uid) + " 查询所有好友动态")
    #     # 调用数据库的接口、
    #     """ trends类
    #       information：
    #           关联映射 server_trends表格
    #       Attributes：
    #           id: 表格主键
    #           uid: 用户关联外键
    #           date: 动态产生日期
    #           article: 动态内容
    #     """
    #     '''
    #     这里需要接入数据库接口
    #     '''
    #     user = trends_my_all_quer(uid)
    #     print(user)
    #     if user:
    #         # result['id'] = id
    #         # result['uid'] = id
    #         # result['date']=date
    #         # result['content']=article
    #         resultContent = []
    #         preparedJson = json.loads(user)
    #         for m in preparedJson:
    #             resultContent.append(m["fields"])
    #             print(m)
    #         print("返回信息:\n" +
    #               "uid " + str(uid) + "\n" +
    #               "resultContent "+str(resultContent)+"\n"+
    #               "isTrends_my_all_querSuccess " + str(True) + "\n"
    #               )
    #         result['resultContent'] = resultContent
    #     result['isTrends_my_all_querSuccess'] = True
    # return JsonResponse(result)


def trends_other_all_querPost(request):
    """
       我的所有请求
       :param: request
       uid
       :return: true   false
       """


    result = {
        'isTrends_other_all_querSuccess': False,
    }
    result['resultContent'] = None

    if request.method == 'POST':
        uid = int(request.POST['uid'])

        fid = relation_my_all_qur(uid)
        # for m in fid:
        #     friends.append(m["fields"])
        resultContent = []

        print("用户名:" + str(uid) + " 查询所有好友动态")
        # 调用数据库的接口、
        """ trends类
          information：
              关联映射 server_trends表格
          Attributes：
              id: 表格主键
              uid: 用户关联外键
              date: 动态产生日期
              article: 动态内容
        """
        '''
        这里需要接入数据库接口
        '''
        for m in fid:

            user = trends_my_all_quer(m["pk"])
            print(user)
            if user:
                # result['id'] = id
                # result['uid'] = id
                # result['date']=date
                # result['content']=article
                preparedJson = json.loads(user)
                for m in preparedJson:
                    resultContent.append(m["fields"])
                    print(m)

        result['resultContent'] = resultContent
        result['isTrends_other_all_querSuccess'] = True
    return JsonResponse(result)