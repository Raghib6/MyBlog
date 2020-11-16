from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contactView,name='contact'),
    path('search/',views.searchQ,name='search'),
    path('blog/<str:pk>/',views.details,name='blog_details'),
    path('create_post/',views.createView,name='create_post'),
    path('update_post/<str:pk>/',views.updateView,name='update_post'),
    path('delete_post/<str:pk>/',views.deleteView,name='delete_post'),
]