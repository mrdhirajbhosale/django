from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'blog', views.BlogsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
