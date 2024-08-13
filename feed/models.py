from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    youtube_video_url = models.URLField(null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    image = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        