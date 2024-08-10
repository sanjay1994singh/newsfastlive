from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('top_header_scroll/', views.top_header_scroll, name='top_header_scroll'),
    path('top_header_news/', views.top_header_news, name='top_header_news'),
]
