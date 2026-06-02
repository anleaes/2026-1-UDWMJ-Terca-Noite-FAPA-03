from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'inspections'

router = routers.SimpleRouter()
router.register('', views.InspectionViewSet, basename='inspections')

urlpatterns = [
    path('<int:construction_id>/list/', views.list_inspection, name='list_inspection'),
    path('<int:construction_id>/add/', views.add_inspection, name='add_inspection'),
    path('<int:construction_id>/edit/<int:id_inspection>/', views.edit_inspection, name='edit_inspection'),
    path('<int:construction_id>/delete/<int:id_inspection>/', views.delete_inspection, name='delete_inspection'),
    path('', include(router.urls)),
]
