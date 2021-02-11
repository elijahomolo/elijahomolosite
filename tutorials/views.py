from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from markdownx.fields import MarkdownxFormField
from .models import Tutorial, Category


class CategoryList(DetailView):
        model = Category
        template_name = 'category_list.html'


        def get_context_data(self, **kwargs):
            context = super(CategoryList, self).get_context_data(**kwargs)
            context['tutorial'] = Tutorial.objects.filter(category=self.object)
            context['category'] = Category.objects.all()
            return context


class TutorialList(DetailView):
        model = Tutorial
        template_name = 'detail_tutorial.html'







# Create your views here.
def index(request):
    latest_tutorial_list = Tutorial.objects.order_by('-pub_date')[:5]
    latest_category_list = Category.objects.order_by('created_at')[:5]
    context = {
        'latest_tutorial_list': latest_tutorial_list,
        'latest_category_list': latest_category_list,
    }
    return render(request, 'tutorials_index.html', context)

def tutorial(request, slug):
    tutorial = get_object_or_404(Tutorial, slug=slug)
    #_t = tutorial.objects.filter(id=tutorial_id).order_by('template').values('template').first()
    #template = _t['detail_blog.html']
    return render(request, 'detail_tutorial.html', {'tutorial': tutorial})
