import redis

from django.shortcuts import get_object_or_404, render
from django.conf import settings

from blog.models import Post

# Create your views here.



r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    print(request.META)
    if request.user.is_authenticated:
        get_user_in_total_view = r.get('post:%s:%s' % (post.id, request.user))
        if not get_user_in_total_view:    
            r.incr('post:%s:%s' % (post.id, request.user))
        else:
            ip_address = request.META['HTTP_HOST']
            get_user_in_total_view = r.get('post:%s:%s' % (post.id, ip_address))
            if not get_user_in_total_view:
                r.incr('post:%s:%s' % (post.id, ip_address))
        total_view = len(r.keys('post:%s:*' % (post.id)))
    return render(request, 'detail.html', {'post': post, 
                                           'total_view': total_view})