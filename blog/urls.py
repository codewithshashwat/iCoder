from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.blogHome,name="blogHome"),
    path('<str:slug>',views.blogPost,name="BlogPost"),
]
