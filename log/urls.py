from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'supermc_register', views.SuperMcRegister, basename='supermc_register')
router.register(r'supermc_contact_list', views.SuperMcContactList, basename='supermc_contact_list')
router.register(r'supermc_verify_user', views.SuperMcVerifyUser, basename='supermc_verify_user')
router.register(r'supermc_reset_key', views.SuperMcResetKey, basename='supermc_reset_key')

urlpatterns = [
    path('', include(router.urls)),
]
