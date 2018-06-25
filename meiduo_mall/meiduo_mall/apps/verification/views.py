from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django_redis import get_redis_connection
from rest_framework.views import APIView

from meiduo_mall.libs.captcha.captcha import captcha


class imagecodeid(APIView):
    def get(self,request,code_id):
        text,image  = captcha.generate_captcha()
        redis_conn = get_redis_connection('verify_codes')
        redis_conn.setex(code_id,60,text)

        return HttpResponse(image,content_type='images/jpg')


