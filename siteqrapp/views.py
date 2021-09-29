from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


from . import forms
from .decoder import get_my_code, get_my_code_test
# from .forms import Camera
# from django.core.cache import cache
from django.db import models
import json

def index(request):
    # form = Camera(request)
    # cache.set('mystringjson', 'printresult')
    shop = request.GET.get("sh", "")
    return render(request, 'siteqrapp/index.html', {'shop': shop})
    # return HttpResponse(request, 'siteqrapp/index.html')

def info(request):
    return render(request, 'siteqrapp/info.html')

def error(request):
    return render(request, 'siteqrapp/error.html')

def test(request):
    # 'intresult' = cache.get('mystringjson')
    # cache.delete('mystringjson')
    return render(request, 'siteqrapp/test.html')


def ggjs(request):
    data = {'msg':''}
    # if request.method == 'GET':
    #     username = request.GET.get('username').lower()
    #     exists = Usernames.objects.filter(name=username).exists()
    #     if exists:
    #         data['msg'] = username + ' already exists.'
    #     else:
    data['msg'] = get_my_code(request)
    return JsonResponse(data)

def printinfo(request):
    # myimg = ('static/img/01.jpg')
    data = {'cont': get_my_code()}
    return render(request, 'siteqrapp/result.html', data)
    # return render(request, 'siteqrapp/printinfo.html', data)

def result(request):
    return render(request, 'siteqrapp/result.html')

def test2(request):
    return render(request, 'siteqrapp/test2.html')

def getDataPhoto(request):
    if request.method == 'POST':

        shop = request.POST.get('shop', None)
        print(shop)
        photo = request.POST.get('photo', None)
        print(shop)
        # request_gdata = request.POST.get('photo,shop', None)
        takingData = get_my_code(photo, shop)

        if takingData == 0:
            return JsonResponse({
                "result": False,
                "js_string": takingData})
        if takingData == 1:
            return JsonResponse({
                "result": False,
                "js_string": takingData})
        # data = {'cont': takingData}
        return JsonResponse({
             "result": True,
             "js_string": takingData})
    else:
        return JsonResponse({
            "result": False,
            "js_string": ''})

