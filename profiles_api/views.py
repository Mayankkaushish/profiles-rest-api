from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from profiles_api import models
from profiles_api import permissions


# Create your views here.
class HelloApiView(APIView):
	"""Test API View"""
	serializer_class = serializers.HelloSerializer

	def get(self,request,format=None):
		"""Returns API list view features"""
		an_apiview=['Red','Yelow','Orange','White']

		return Response({'message':'Hello','an_apiview': an_apiview})

	def post(self,request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'
			return Response({'message':message})
		else:
			return Response(serializer.errors, 
				status = status.HTTP_400_BAD_REQUEST)

	def put(self,request,pk=None):
		return Response({'method':'PUT'})

	def patch(self,request,pk=None):
		return Response({'method':'PATCH'})

	def delete(self,request,pk=None):
		return Response({'method':'DELETE'})


class Helloviewset(viewsets.ViewSet):
	serializer_class = serializers.HelloSerializer
	def list(self, request):
		a_viewlist = ['Black','Double Black', 'Gold']
		return Response({'message':'Hello','a_viewlist': a_viewlist})

	def create(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'
			return Response({'message':message})
		else:
			return Response(serializer.errors, 
				status = status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		return Response({'HTTP method':'GET'})

	def update(self, request, pk=None):
		return Response({'HTTP method':'PUT'})

	def partial_update(self, request, pk=None):
		return Response({'HTTP method':'PATCH'})

	def destroy(self, request, pk=None):
		return Response({'HTTP method':'Delete'})

class UserProfileViewset(viewsets.ModelViewSet):
	serializer_class=serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UserProfilePermissions,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','email')
