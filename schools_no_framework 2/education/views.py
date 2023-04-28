import django_filters
from django.http import HttpResponse
from rest_framework.response import Response

from education.serializers import *
from education.models import *
import json

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

class SchoolViewset(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = SchoolSerializer

   def list(self, request, format=None):
       return Response([])


class SClassViewset(viewsets.ModelViewSet):
   queryset = SClass.objects.all()
   serializer_class = SClassSerializer
   filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
   filterset_fields = ["grade", "school_id"]


class StudentViewest(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer
   permission_classes = [permissions.AllowAny]

   def get_queryset(self):
       queryset = Student.objects.all()
       school_id = self.request.query_params.get('school_id', None)
       sclass_id = self.request.query_params.get('class_id', None)
       if school_id is not None:
           queryset = queryset.filter(sclass__school_id=school_id)
       if sclass_id is not None:
           queryset = queryset.filter(sclass_id=sclass_id)
       return queryset



def schools(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps([
            {
                "id":school.id,
                "address":school.address,
                "name":school.name
            } for school in School.objects.all()
        ]))
    if request.method == 'POST':
        # Нужно извлечь параметы из тела запроса
        json_params = json.loads(request.body)

        school = School.objects.create(
            name=json_params['name'],
            address=json_params['address']
        )
        return HttpResponse(json.dumps({
            "id":school.id,
            "name":school.name,
            "school":school.name
        }))


def school_id(request, school_id):
    school = School.objects.get(id=school_id)
    if request.method == 'GET':
        return HttpResponse(json.dumps(
             {
                "id":school.id,
                "address":school.address,
                "name":school.name
            }))
    json_params = json.loads(request.body)
    if request.method == 'PUT':
        school.address = json_params['address']
        school.name = json_params['name']
        school.save()
        return HttpResponse(json.dumps({
            "id":school.id,
            "name":school.name,
            "school":school.name
        }))
    if request.method == 'PATCH':
        school.address = json_params.get('address',school.address)
        school.name = json_params.get('name',school.name)
        school.save()
        return HttpResponse(json.dumps({
            "id":school.id,
            "name":school.name,
            "school":school.name
        }))
    if request.method == 'DELETE':
        school.delete();
        return HttpResponse(json.dumps({}))
