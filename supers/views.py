from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import SuperSerializer
from .models import Super
from super_types.models import Super_Type





@api_view(['GET','POST'])
def supers_list(request):


    supers = Super.objects.all()
    if request.method == 'GET':
        
        super_type_name = request.query_params.get('type')
        
        custom_response_dictionary = {}



        if super_type_name:
            supers = supers.filter(super_type__type=super_type_name)

        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)


    if request.method == "GET":
        serializer = SuperSerializer(super)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)