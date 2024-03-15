from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import CreateAPIView

from vehicle.models import Car, Moto, Milage
from vehicle.serializers import CarSeriliazer, MotoSeriliazer, MilageSeriliazer, MotoMilageSerializer, \
    MotoCreateSerializer


# Create your views here.


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSeriliazer
    queryset = Car.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSeriliazer
    queryset = Moto.objects.all()


class MotoRetrievePIView(generics.RetrieveAPIView):
    serializer_class = MotoSeriliazer
    queryset = Moto.objects.all()


class MotoUpdatePIView(generics.UpdateAPIView):
    serializer_class = MotoSeriliazer
    queryset = Moto.objects.all()


class MotoDestroyPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MilageCreateAPIView(CreateAPIView):
    serializer_class = MilageSeriliazer


class MotoMilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer
