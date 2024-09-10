from django.urls import path
from . import views

urlpatterns = [
    path('live_stream/', views.live_stream, name='live_stream'),
]
