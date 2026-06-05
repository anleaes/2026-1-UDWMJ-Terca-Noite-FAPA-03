from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api-login/', views.api_login, name='api_login'),
    path('api-me/', views.api_me, name='api_me'),
    path('api-logout/', views.api_logout, name='api_logout'),
]
