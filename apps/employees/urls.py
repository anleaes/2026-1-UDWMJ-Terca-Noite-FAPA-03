from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'employees'

router = routers.SimpleRouter()
router.register('', views.EmployeeViewSet, basename='employees')

urlpatterns = [
    path('<int:company_id>/list/', views.list_employees, name='list_employees'),
    path('<int:company_id>/add/', views.add_employee, name='add_employee'),
    path('<int:company_id>/edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('<int:company_id>/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('', include(router.urls)),
]
