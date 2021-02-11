from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category
from markdownx.fields import MarkdownxFormField



class CategoryList(DetailView):
        model = Category
        template_name = 'blog_category_list.html'

        def get_context_data(self, **kwargs):
            context = super(CategoryList, self).get_context_data(**kwargs)
            context['post'] = Post.objects.filter(category=self.object)
            context['category'] = Category.objects.all()
            return context

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    latest_category_list = Category.objects.order_by('created_at')[:5]
    context = {
        'latest_post_list': latest_post_list,
        'latest_category_list': latest_category_list,
    }
    return render(request, 'index.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    #_t = Post.objects.filter(id=post_id).order_by('template').values('template').first()
    #template = _t['detail_blog.html']
    return render(request, 'detail_blog.html', {'post': post})
