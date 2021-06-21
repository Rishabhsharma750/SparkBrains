from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def student_details(request,num):
    stu=Student.objects.get(id=num)
    serializer=StudentSerializer(stu,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def student_update(request,num):
    stu = Student.objects.get(id=num)
    serializer = StudentSerializer(instance=stu,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def student_delete(request,num):
    stu=Student.objects.get(id=num)
    stu.delete()
    return Response('Item successfully deleted')