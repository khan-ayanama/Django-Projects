from django.contrib import admin
from news.models import News

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_content')


admin.site.register(News, NewsAdmin)
