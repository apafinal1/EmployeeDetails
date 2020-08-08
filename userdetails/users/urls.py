
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('final/', views.EmployeeAPIView.as_view(),name="book"),
    path('detail/<int:pk>/', views.EmployeeDetails.as_view(), name="detail"),
]
