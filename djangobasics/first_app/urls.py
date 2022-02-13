from django.urls import path
from first_app import views
from django.urls import re_path,include

urlpatterns = [
   re_path(r'^$',views.index,name='index'),
   re_path(r'^help',views.help,name='help'),
]
