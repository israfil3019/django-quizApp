from django.shortcuts import HttpResponse
from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



def home(request):
    return HttpResponse('<h1>Home Page</h1>')


@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
      
        return Response(serializer.data)
  