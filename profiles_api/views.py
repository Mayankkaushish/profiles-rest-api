from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status

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