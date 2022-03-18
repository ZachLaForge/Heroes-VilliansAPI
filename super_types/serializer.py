from rest_framework import serializers
from .models import Super_Type

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super_Type
        fields = ['id', 'type']

        type = serializers.IntegerField(write_only=True)