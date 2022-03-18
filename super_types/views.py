from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import SuperTypeSerializer
from .models import Super_Type



@api_view(['GET', 'POST'])
def super_types_list(request):
    if request.method == 'GET':
        supers = Super_Type.objects.all()
        serializer = SuperTypeSerializer(supers, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def super_type_detail(request, pk):
    super = get_object_or_404(Super_Type, pk=pk)


    if request.method == "GET":
        serializer = SuperTypeSerializer(super)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


