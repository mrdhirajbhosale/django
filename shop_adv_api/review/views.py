from rest_framework import viewsets
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.response import Response


# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        shop = Review.objects.all()
        serializer = ReviewSerializer(shop, many=True)
        return Response(serializer.data)
