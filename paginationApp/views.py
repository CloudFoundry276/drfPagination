from django.shortcuts import render
from paginationApp.models import Student
from paginationApp.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


# Create your views here.
class StudentPagination(PageNumberPagination):
    page_size = 1

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination
