from rest_framework import serializers  # type: ignore[import]
from .models import *

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['id', 'name', 'description', 'created_at']
