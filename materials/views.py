import generics as generics
from django.shortcuts import render
from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()




class LessonRetrievePIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdatePIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()