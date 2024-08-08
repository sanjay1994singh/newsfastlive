from django.shortcuts import render

from news.models import News


# Create your views here.
def details(request, id):
    news = News.objects.get(id=id)
    context = {
        'news': news
    }
    return render(request, 'details.html', context)
