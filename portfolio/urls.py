from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
#    path('<int:portfolio_id>/', views.portfolio, name='portfolio'),
]
