from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post, Category
from markdownx.fields import MarkdownxFormField



# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'index.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    #_t = Post.objects.filter(id=post_id).order_by('template').values('template').first()
    #template = _t['detail_blog.html']
    return render(request, 'detail_blog.html', {'post': post})
