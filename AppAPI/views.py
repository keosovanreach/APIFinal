from rest_framework import generics  # type: ignore[reportMissingImports]
from .models import *
from .serializers import RolesSerializer

# Create your views here.
class RolesListCreate(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class RolesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):        
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer



