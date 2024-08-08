from django.contrib import admin
from .models import News, Category, OtherNewsImage

# Register your models here.

admin.site.register(Category)
admin.site.register(News)
admin.site.register(OtherNewsImage)
