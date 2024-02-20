from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem
from rest_framework.decorators import api_view
import json
from django.core import serializers

# Create your views here.

def home(request):
    return HttpResponse('Hello World')

@api_view(['POST'])
def AddNewToDoItem(request):
    received_json_data=json.loads(request.body)
    print(received_json_data)
    dbo = ToDoItem(name = received_json_data['name'], isdone=False)
    dbo.save()
    return HttpResponse(serializers.serialize('json', [dbo]))

@api_view(['PUT'])
def UpdateItemStatus(request):
    id=request.GET.get('id', '')
    isdone=request.GET.get('isdone', False)
    dbo = ToDoItem.objects.filter(pk=id).update(isdone=isdone)
    return HttpResponse(dbo)

@api_view(['GET'])
def GetAllItems(request):
    dbo = ToDoItem.objects.all()
    return HttpResponse(serializers.serialize('json', dbo))

@api_view(['DELETE'])
def RemoveItem(request):
    id=request.GET.get('id', '')
    dbo = ToDoItem.objects.filter(id=id).delete()
    return HttpResponse(dbo)