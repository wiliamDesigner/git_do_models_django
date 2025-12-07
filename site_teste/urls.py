from django.contrib import admin
from django.urls import path
from core.views import hello_post, hello_form, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_post),
    path('form/', hello_form),
    path('', index),  
]
