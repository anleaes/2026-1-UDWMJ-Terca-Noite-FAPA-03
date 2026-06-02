from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'constructions'

router = routers.SimpleRouter()
router.register('', views.ConstructionViewSet, basename='constructions')

urlpatterns = [
    path('add/', views.add_construction, name='add_construction'),
    path('list/', views.list_constructions, name='list_constructions'),
    path('edit/<int:id_construction>/', views.edit_construction, name='edit_construction'),
    path('delete/<int:id_construction>/', views.delete_construction, name='delete_construction'),
    path('', include(router.urls)),
]
