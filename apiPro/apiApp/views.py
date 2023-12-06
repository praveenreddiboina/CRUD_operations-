from django.shortcuts import render
from .models import Employee 
from .serializers import Employeeserializers
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = Employeeserializers(employees,many=True)
        return JsonResponse({'employees':serializer.data})
    if request.method == 'POST':
        serializer = Employeeserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def employee_details(request,id):
    try:
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Employeeserializers(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Employeeserializers(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
         