from django.shortcuts import render

# Create your views here.
# 必须返回一个响应
from django.http import HttpResponse

def index(request):
    #  return HttpResponse('ok')
    #  render 第一个参数是请求 第二个参数是html位置，因为在seting中已经设置模板的位置在template,所以参数不用
    return render(request,'book/index.html')
