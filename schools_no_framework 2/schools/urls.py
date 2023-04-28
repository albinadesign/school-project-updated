"""NewsPaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import include, path
from education import views
from django.views.generic import TemplateView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'schools', views.SchoolViewset)
router.register(r'classes', views.SClassViewset)
router.register(r'students', views.StudentViewest)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schools', views.schools),
    path('schools/<int:school_id>', views.school_id),
    path('swagger-ui/', TemplateView.as_view(
      template_name='swagger-ui.html',
      extra_context={'schema_url': 'openapi-schema'}
   ), name='swagger-ui'),
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
