from django.shortcuts import render

from news.models import News


# Create your views here.
def homepage(request):
    news = News.objects.all().order_by('-id')
    context = {
        'news': news
    }
    return render(request, 'homepage.html', context)
