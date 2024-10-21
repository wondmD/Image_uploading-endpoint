from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhotoViewSet, CustomAuthToken

router = DefaultRouter()
router.register(r'photos', PhotoViewSet, basename='photos')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view()),  # Endpoint for obtaining a token
]
