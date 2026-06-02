from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'citizens'

router = routers.SimpleRouter()
router.register('', views.CitizenViewSet, basename='citizens')

urlpatterns = [
    path('add/', views.add_citizen, name='add_citizen'),
    path('list/', views.list_citizens, name='list_citizens'),
    path('edit/<int:id_citizen>/', views.edit_citizen, name='edit_citizen'),
    path('delete/<int:id_citizen>/', views.delete_citizen, name='delete_citizen'),
    path('', include(router.urls)),
]
