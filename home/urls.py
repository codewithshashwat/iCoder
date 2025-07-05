from django.urls import include, path
from home import views

urlpatterns = [
    path('contact',views.contact,name="Contact"),
    path('about',views.about,name="About"),
    path('',views.home,name="Home"),
    path('search', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]
