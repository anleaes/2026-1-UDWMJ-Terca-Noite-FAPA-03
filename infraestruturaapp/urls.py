"""
URL configuration for infraestruturaapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('companies/', include('companies.urls', namespace='companies')),
    path('citizens/', include('citizens.urls', namespace='citizens')),
    path('constructions/', include('constructions.urls', namespace='constructions')),
    path('contracts/', include('contracts.urls', namespace='contracts')),
    path('locations/', include('locations.urls', namespace='locations')),
    path('equipments/', include('equipments.urls', namespace='equipments')),
    path('incidents/', include('incidents.urls', namespace='incidents')),
    path('inspections/', include('inspections.urls', namespace='inspections')),
    path('audit-reports/', include('audit_reports.urls', namespace='audit_reports')),
    path('constructionequipments/', include('constructionequipments.urls', namespace='constructionequipments')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
