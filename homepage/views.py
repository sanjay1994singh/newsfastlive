from django.http import JsonResponse
from django.shortcuts import render

from news.models import News

from live_streaming.models import LiveStreaming


# Create your views here.
def homepage(request):
    news = News.objects.all().order_by('-id')
    # top tranding news ----
    first_news = news[0]
    top_other_tranding = news[1:4]
    # end top tranding news ----

    crime_news = news.filter(category__name='Crime')[:5]

    live_data = LiveStreaming.objects.filter(code='live_streaming')
    print(live_data, '==================================live_data')
    context = {
        'first_news': first_news,
        'other_top': top_other_tranding,
        'crime_news': crime_news,
        'live_data': live_data[0].text,
    }
    return render(request, 'homepage.html', context)


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
