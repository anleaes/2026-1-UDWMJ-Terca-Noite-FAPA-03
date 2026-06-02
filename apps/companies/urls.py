from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'companies'

router = routers.SimpleRouter()
router.register('', views.CompanyViewSet, basename='companies')

urlpatterns = [
    path('add/', views.add_company, name='add_company'),
    path('list/', views.list_companies, name='list_companies'),
    path('edit/<int:id_company>/', views.edit_company, name='edit_company'),
    path('delete/<int:id_company>/', views.delete_company, name='delete_company'),
    path('', include(router.urls)),
]
