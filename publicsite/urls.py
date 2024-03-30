from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('google-signup',views.google_signup,name='google-signup'),
    path('logout',views.logout,name='logout')
]
