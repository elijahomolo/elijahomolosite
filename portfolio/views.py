from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Portfolio


# Create your views here.
def index(request):
    latest_portfolio_list = Portfolio.objects.order_by('-pub_date')[:5]
    context = {
        'latest_portfolio_list': latest_portfolio_list,
    }
    return render(request, 'portfolio_index.html', context)
