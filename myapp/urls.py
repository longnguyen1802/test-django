from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('apilogin', views.apilogin, name='apilogin'),
    path('authenticate', views.authenticate, name='authenticate'),
    path('logout', views.logout, name='logout'),
    path('', views.dashboard, name='index'),
]