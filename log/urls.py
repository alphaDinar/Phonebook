from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'supermc_register', views.SuperMcRegister, basename='supermc_register')
router.register(r'supermc_check_register', views.SuperMcCheckRegister, basename='supermc_check_register')

urlpatterns = [
    path('', include(router.urls)),
]
