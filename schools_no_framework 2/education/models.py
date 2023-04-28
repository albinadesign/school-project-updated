from django.db import models
from rest_framework import status
from rest_framework.response import Response


class School(models.Model):
    name = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    def destroy(self, request, pk, format=None):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SClass(models.Model):
    grade = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=64)
    sclass = models.ForeignKey(SClass, on_delete=models.CASCADE)
