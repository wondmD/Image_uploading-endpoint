from django.contrib import admin
from django.urls import path, include
from core.views import PhotoViewSet, CustomAuthToken
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'photos', PhotoViewSet, basename='photos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', CustomAuthToken.as_view()), 
]


