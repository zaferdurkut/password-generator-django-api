from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework import serializers, viewsets, routers


router = routers.DefaultRouter()
router.register(r'passwords', views.PasswordViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'create_password',views.create_password),
    path(r'create_and_save_password',views.create_and_save_password),
    path(r'create_password_with_image',views.create_password_with_image),
    path(r'create_and_save_password_with_image',views.create_and_save_password_with_image),
    url(r'^health_check/', include('health_check.urls')),

]
