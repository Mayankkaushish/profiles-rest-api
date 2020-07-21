from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
	"""Test API View"""
	def get(self,request,format=None):
		"""Returns API list view features"""
		an_apiview=['Red','Yelow','Orange','White']

		return Response({'message':'Hello','an_apiview': an_apiview})
