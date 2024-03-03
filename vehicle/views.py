from django.shortcuts import render
from rest_framework import viewsets, generics
from vehicle.models import Car, Moto
from vehicle.seriliazers import CarSeriliazer, MotoSeriliazer


# Create your views here.


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSeriliazer
    queryset = Car.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoSeriliazer


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
