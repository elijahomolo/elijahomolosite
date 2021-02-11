from . import views
from django.urls import path, include
from .views import CategoryList, TutorialList


urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', TutorialList.as_view(), name='tutoriallist'),
    path('category/<slug:slug>', CategoryList.as_view(), name='categorylist'),
    path('markdownx/', include('markdownx.urls')),
]
