from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'constructionequipments'

router = routers.SimpleRouter()
router.register('', views.ConstructionEquipmentViewSet, basename='constructionequipments')

urlpatterns = [
    path('<int:construction_id>/list/', views.list_constructionequipment, name='list_constructionequipment'),
    path('<int:construction_id>/add/', views.add_constructionequipment, name='add_constructionequipment'),
    path('<int:construction_id>/edit/<int:constructionequipment_id>/', views.edit_constructionequipment, name='edit_constructionequipment'),
    path('<int:construction_id>/delete/<int:constructionequipment_id>/', views.delete_constructionequipment, name='delete_constructionequipment'),
    path('', include(router.urls)),
]
