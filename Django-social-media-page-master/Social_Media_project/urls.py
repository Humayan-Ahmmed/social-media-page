from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from App_posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('App_login.urls')),
    path('posts/',include('App_posts.urls')),
    path('',views.home,name='home'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
