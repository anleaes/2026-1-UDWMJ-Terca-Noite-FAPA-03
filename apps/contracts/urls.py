from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'contracts'

router = routers.SimpleRouter()
router.register('', views.ContractViewSet, basename='contracts')

urlpatterns = [
    path('add/<int:construction_id>/', views.add_contract, name='add_contract'),
    path('list/<int:construction_id>/', views.list_contracts, name='list_contracts'),
    path('edit/<int:construction_id>/<int:id_contract>/', views.edit_contract, name='edit_contract'),
    path('delete/<int:construction_id>/<int:id_contract>/', views.delete_contract, name='delete_contract'),
    path('', include(router.urls)),
]
