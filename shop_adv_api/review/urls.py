from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'shop', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
