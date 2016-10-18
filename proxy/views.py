from django.shortcuts import render
import requests
from django.http import HttpResponse

def index(request):
    url = request.GET.get('url')
    proxy = request.GET.get('proxy')
    print('url:', url)
    print('proxy:', proxy)
    proxies = { "http" : 'http://' + proxy ,
                "https" : 'https://' + proxy }
    r = requests.get(url, proxies = proxies)
    print('status:', r.status_code)
    text = r.text.encode('utf-8')
    return HttpResponse(text)

