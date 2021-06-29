from django.shortcuts import render
from .models import *
from api import permissions
from .serializer import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields=('name','email',)

class UserViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'city',)

# class UserViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Student.objects.all()
#         serializer = StudentSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         stu = Student.objects.get(id=pk)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Student.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = StudentSerializer(user)
#         return Response(serializer.data)
#
#     def destroy(self,request,pk):
#         stu=Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data deleted'})

class UserLoginView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



#
# @api_view(['GET'])
# def url_list(request):
#     api_url={
#         'List':'list/',
#         'Detail':'details/<int:num>/',
#         'Create':'create/',
#         'Update':'update/<int:num>/',
#         'Delete':'delete/<int:num>/',
#     }
#     return Response(api_url)
#
# @api_view(['GET'])
# def student_list(request):
#     stu=Student.objects.all()
#     serializer=StudentSerializer(stu,many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def student_details(request,num):
#     stu=Student.objects.get(id=num)
#     serializer=StudentSerializer(stu,many=False)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def student_create(request):
#     serializer=StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# @api_view(['PUT'])
# def student_update(request,num):
#     stu = Student.objects.get(id=num)
#     serializer = StudentSerializer(instance=stu,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# @api_view(['DELETE'])
# def student_delete(request,num):
#     stu=Student.objects.get(id=num)
#     stu.delete()
#     return Response('Item successfully deleted')