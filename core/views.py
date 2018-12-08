from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import requests, json, itertools

def home(request):
    api_requests = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_requests.content)

    page = request.GET.get('page', 1)

    paginator = Paginator(api['Data'], 6)

    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    return render(request,'home.html', {
        'news_list': news_list
    })
