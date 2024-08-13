from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect, reverse

from .models import Feed, UserReaction


def home(request):
    feeds = Feed.objects.order_by('-published_at')[:10]
    return render(request, 'feed/home.html', {'feeds': feeds})


def detail(request, feed_id):
    feed = get_object_or_404(Feed, id=feed_id)
    feed.view_count += 1
    feed.save()
    return render(request, 'feed/detail.html', {'feed': feed})


@login_required
def like_feed(request, feed_id):
    feed = get_object_or_404(Feed, id=feed_id)
    reaction, created = UserReaction.objects.get_or_create(
        user=request.user, feed=feed)

    if not created and reaction.is_like:
        return redirect(reverse('feed:detail', args=[feed_id]))

    if not created and not reaction.is_like:
        feed.dislikes -= 1

    feed.likes += 1
    reaction.is_like = True
    feed.save()
    reaction.save()

    return redirect(reverse('feed:detail', args=[feed_id]))


@login_required
def dislike_feed(request, feed_id):
    feed = get_object_or_404(Feed, id=feed_id)
    reaction, created = UserReaction.objects.get_or_create(
        user=request.user, feed=feed)

    if not created and not reaction.is_like:
        return redirect(reverse('feed:detail', args=[feed_id]))

    if not created and reaction.is_like:
        feed.likes -= 1

    feed.dislikes += 1
    reaction.is_like = False
    feed.save()
    reaction.save()

    return redirect(reverse('feed:detail', args=[feed_id]))
