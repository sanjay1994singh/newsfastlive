from django.http import JsonResponse
from django.shortcuts import render

from live_streaming.models import LiveStreaming
import random


# Create your views here.
def live_stream(request):
    if request.method == 'GET':

        form = request.GET
        id = form.get('live_id')
        view_count = LiveStreaming.objects.get(id=id)
        switch_button = view_count.switch_button
        if switch_button is True:
            random_number = random.randint(3, 7)
        else:
            random_number = 1
        new_count = int(view_count.views_count) + random_number
        view_count.views_count = new_count
        view_count.save()

        context = {
            'view_count': view_count.views_count
        }
        return JsonResponse(context)
