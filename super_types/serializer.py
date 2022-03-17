from rest_framework import serializers
from .models import Super_Type

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super_Type
        fields = ['id', 'type'] 