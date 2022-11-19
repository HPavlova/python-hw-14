from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter_by_author', views.filter_by_author, name='filter_by_author'),
]
