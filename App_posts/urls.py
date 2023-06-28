from django.urls import path
from App_posts import views
app_name='App_posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('liked/<pk>/',views.liked,name='liked'),
    path('unlike/<pk>/',views.unlike,name='unlike'),


]

