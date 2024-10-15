from . import views
from django.urls import path

urlpatterns = [
    path('', views.url_shortener, name='url_shortener'),
]