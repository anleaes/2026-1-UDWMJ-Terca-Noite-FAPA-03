from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'locations'

router = routers.SimpleRouter()
router.register('', views.LocationViewSet, basename='locations')

urlpatterns = [
    path('add/', views.add_location, name='add_location'),
    path('list/', views.list_location, name='list_location'),
    path('edit/<int:id_location>/', views.edit_location, name='edit_location'),
    path('delete/<int:id_location>/', views.delete_location, name='delete_location'),
    path('', include(router.urls)),
]
