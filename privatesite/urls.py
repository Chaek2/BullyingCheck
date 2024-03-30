from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('google_responce', views.google_responce, name='google_responce'),
]
