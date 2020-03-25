from rest_framework import viewsets
from .serializers import ShopSerializer
from .models import Shop
from rest_framework.response import Response


# Create your views here.

class ShopViewSet(viewsets.ModelViewSet, viewsets.ViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def list(self, request, *args, **kwargs):
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True)
        return Response(serializer.data)
