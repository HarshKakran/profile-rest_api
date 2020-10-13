from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from . import serializers
from .models import UserProfile
from . import permissions

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

class HelloViewSet(viewsets.ViewSet):
    #TEst api viewset

    serializers_class = serializers.HelloSerializer

    def list(self,request):
        #Returns something to test
        a_viewset = [
            "something ",
            "is ",
            "going",
            'on'
        ]
        return Response({'a_viewset':a_viewset})

    def create(self,request):
        #Create a new message

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            return Response({'message':'Hello {0}'.format(name)})
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # USed to get object

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        # Used to update objects

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        # Used to update a particular part of the object

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        #Used to delete the object

        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
     # Handles creating, reading, and updating profiles

     serializer_class = serializers.UserProfileSerializer
     queryset = UserProfile.objects.all()

     authentication_classes = (TokenAuthentication,)
     permission_classes = (permissions.UpdateOwnProfile,)
     filter_backends = (filters.SearchFilter,)
     search_fields = ('name','email',)