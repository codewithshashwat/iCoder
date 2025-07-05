from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "iCoder Admin"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome onboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('blog/',include('blog.urls'))
]
