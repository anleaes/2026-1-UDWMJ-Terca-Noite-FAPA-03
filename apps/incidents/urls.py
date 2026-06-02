from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'incidents'

router = routers.SimpleRouter()
router.register('', views.IncidentViewSet, basename='incidents')

urlpatterns = [
    path('add/', views.add_incident, name='add_incident'),
    path('list/', views.list_incidents, name='list_incidents'),
    path('edit/<int:id_incident>/', views.edit_incident, name='edit_incident'),
    path('delete/<int:id_incident>/', views.delete_incident, name='delete_incident'),
    path('', include(router.urls)),
]
