from django.contrib import admin
from .models import Feed


class FeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'view_count', 'likes', 'dislikes')


admin.site.register(Feed, FeedAdmin)
