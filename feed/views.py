from django.shortcuts import get_object_or_404, render

from .models import Feed


def home(request):
    feeds = Feed.objects.order_by('-published_at')[:10]
    return render(request, 'feed/home.html', {'feeds': feeds})

def detail(request, feed_id):
    feed = get_object_or_404(Feed, id=feed_id)
    feed.view_count += 1
    feed.save()
    return render(request, 'feed/detail.html', {'feed': feed})
