from django.shortcuts import render

from news.models import News


# Create your views here.
def detail(request, id):
    news = News.objects.get(id=id)
    count = news.count + 1
    news.count = count
    news.save()

    news = News.objects.get(id=id)
    absolute_image_url = request.build_absolute_uri(news.featured_image.url)
    context = {
        'news': news,
        'absolute_image_url': absolute_image_url,
    }
    return render(request, 'details.html', context)
