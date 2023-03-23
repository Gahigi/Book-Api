from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

# Create your views here.
class ViewAllBooks(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializers_data = BookSerializer(books, many=True)
        return Response(serializers_data.data, status= status.HTTP_200_OK)
    def post(self, request):
        serializers_data = BookSerializer(data= request.data)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response(serializers_data.data, status= status.HTTP_201_CREATED)
        return Response(serializers_data.errors, status= status.HTTP_400_BAD_REQUEST)
    
class ViewBook(APIView):
     def get(self, request, id):
         book = Book.objects.get(id = id)
         serializers_data = BookSerializer(book)
         return Response(serializers_data.data, status= status.HTTP_200_OK)   
     def put(self, request, id):
         book = Book.objects.get(id = id)
         serializers_data = BookSerializer(book, data= request.data)
         if serializers_data.is_valid():
             serializers_data.save()
             return Response(serializers_data.data, status= status.HTTP_201_CREATED)
         return Response(serializers_data.errors, status= status.HTTP_400_BAD_REQUEST)
     def delete(self, request, id):
         book = Book.objects.get(id =id)
         book.delete()
         return Response({"status: Deleted"})
    
     
         