from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post, name='post'),
    path('markdownx/', include('markdownx.urls')),
]
