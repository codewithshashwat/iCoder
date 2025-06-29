from django.urls import include, path
from home import views

urlpatterns = [
    path('contact',views.contact,name="Contact"),
    path('about',views.about,name="About"),
    path('',views.home,name="Home"),
]
