from django.shortcuts import render

# Create your views here.
# 必须返回一个响应
from django.http import HttpResponse

def index(request):
    return HttpResponse('ok')
