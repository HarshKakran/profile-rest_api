from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    #Test API View

    def get(request, self, format=None):
        #Returns a list

        list = ['Hello',
                'How are you',
                'What are you doing']

        return Response({'list':list})