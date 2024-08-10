from django.http import JsonResponse
from django.shortcuts import render

from news.models import News


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def top_header_scroll(request):
    news = News.objects.all().order_by('-id')[:4]
    news_list = []
    for i in news:
        data_dict = {}
        data_dict['id'] = i.id
        data_dict['title'] = i.title
        news_list.append(data_dict)
    context = {
        'news': news_list
    }
    return JsonResponse(context)


def top_header_news(request):
    news = News.objects.all().order_by('-id')[:4]
    news_list = []
    for i in news:
        data_dict = {}
        data_dict['id'] = i.id
        data_dict['category'] = i.category.name
        data_dict['title'] = i.title
        data_dict['text'] = i.text
        data_dict['featured_image'] = i.featured_image.url
        data_dict['created_at'] = i.created_at
        news_list.append(data_dict)
    context = {
        'news': news_list
    }
    return JsonResponse(context)
