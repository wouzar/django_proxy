from django.shortcuts import render
import requests
from django.http import HttpResponse

def index(request):
    url = request.GET.get('url')
    proxy = request.GET.get('proxy')
    print(url)
    print(proxy)
    proxies = { "http" : proxy }
    r = requests.get(url, proxies = proxies)
    text = r.text.encode('utf-8')
    return HttpResponse(text)

