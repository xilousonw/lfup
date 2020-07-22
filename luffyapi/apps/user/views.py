from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from . import serializer
from luffyapi.utils.response import APIResponse
from rest_framework.decorators import action
from . import models
class LoginView(ViewSet):
    @action(methods=['POST'],detail=False)
    def login(self,request,*args,**kwargs):
        ser=serializer.UserSerilaizer(data=request.data)
        if ser.is_valid():
            token=ser.context['token']
            #ser.context['user'] 是user对象
            username=ser.context['user'].username
            # {'code':1
            #  msg:'chengg'
            #  token:'sdfasdf'
            #  username:'root'
            #  }
            return APIResponse(token=token,username=username)
        else:
            return APIResponse(code=0,msg=ser.errors)

    @action(methods=['GET'], detail=False)
    def check_telephone(self,request,*args,**kwargs):
        import re
        telephone=request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}',telephone):
            return APIResponse(code=0,msg='手机号不合法')
        try:
            models.User.objects.get(telephone=telephone)
            return APIResponse(code=1)
        except:
            return APIResponse(code=0,msg='手机号不存在')








