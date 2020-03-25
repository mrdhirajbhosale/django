from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response


# Create your views here.

class UserViewSet(viewsets.ModelViewSet, viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
