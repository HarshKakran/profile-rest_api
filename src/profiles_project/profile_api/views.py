from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
class HelloApiView(APIView):
    #Test API View

    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        #Returns a list

        list = ['Hello',
                'How are you',
                'What are you doing']

        return Response({'list':list})

    def post(self, request):
        #Create a hello message with the user entered name

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
    def put(self, request,pk=None):
        #Handles the put requests i.e., update the api

        return Response({'methods':'put'})

    def patch(self, request, pk=None):
        # USed to update a specific part of the api

        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        #used to delete

        return Response({'method':'delete'})