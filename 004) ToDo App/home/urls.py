from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('AddNewToDoItem', views.AddNewToDoItem),
    path('UpdateItemStatus', views.UpdateItemStatus),
    path('GetAllItems', views.GetAllItems),
    path('RemoveItem', views.RemoveItem)
]