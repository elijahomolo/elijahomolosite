from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Category


# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'index.html', context)
