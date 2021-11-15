from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('content/', views.content, name='content'),
    path('contact/', views.contact, name='contact'),
    path('mail/', views.mail, name='mail')
]
