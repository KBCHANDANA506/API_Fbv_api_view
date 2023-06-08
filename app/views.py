from django.shortcuts import render

# Create your views here.
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])

def Employee_JData(request):
    EQS=Employee.objects.all()
    EJD=EmployeeMS(EQS,many=True)


    return Response(EJD.data)