from . import views
from django.urls import path, include
from .views import CategoryList


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post, name='post'),
    path('category/<slug:slug>', CategoryList.as_view(), name='categorylist'),
    path('markdownx/', include('markdownx.urls')),
]
