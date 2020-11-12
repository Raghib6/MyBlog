from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('blog/',views.blog,name='blog'),
    path('search/',views.searchQ,name='search'),
    path('blog/<str:pk>/',views.details,name='blog_details'),
]