from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Tutorial, Category


# Create your views here.
def index(request):
    latest_tutorial_list = Tutorial.objects.order_by('-pub_date')[:5]
    context = {
        'latest_tutorial_list': latest_tutorial_list,
    }
    return render(request, 'tutorials_index.html', context)

def tutorial(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    #_t = tutorial.objects.filter(id=tutorial_id).order_by('template').values('template').first()
    #template = _t['detail_blog.html']
    return render(request, 'detail_tutorial.html', {'tutorial': tutorial})
