from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.generics import CreateAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsOwner, IsModerator
from vehicle.models import Car, Moto, Milage
from vehicle.permissions import IsOwnerOrStaff
from vehicle.serializers import CarSeriliazer, MotoSeriliazer, MilageSeriliazer, MotoMilageSerializer, \
    MotoCreateSerializer


# Create your views here.


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSeriliazer
    queryset = Car.objects.all()
    permission_classes_by_action = {'create': [IsAuthenticated, ~IsModerator],
                                    'list': [IsAuthenticated, IsOwner],
                                    'retrieve': [IsAuthenticated, IsOwner],
                                    'update': [IsAuthenticated, IsOwner],
                                    'destroy': [IsAuthenticated, IsOwner],
                                    }

    def perform_create(self, serializer):
        car_moto = serializer.save()
        car_moto.owner = self.request.user
        car_moto.save()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_moto = serializer.save()
        new_moto.owner = self.request.user
        new_moto.save()



class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSeriliazer
    queryset = Moto.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class MotoRetrievePIView(generics.RetrieveAPIView):
    serializer_class = MotoSeriliazer
    queryset = Moto.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class MotoUpdatePIView(generics.UpdateAPIView):
    serializer_class = MotoSeriliazer
    queryset = Moto.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]



class MotoDestroyPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()
    permission_classes = [IsAuthenticated, IsOwner, ~IsModerator]


class MilageCreateAPIView(CreateAPIView):
    serializer_class = MilageSeriliazer
    permission_classes = [IsAuthenticated, ~IsModerator]


class MotoMilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer
    permission_classes = [IsAuthenticated]


class MilageListAPIView(generics.ListAPIView):
    serializer_class = MilageSeriliazer
    queryset = Milage.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_fields = ('car', 'moto')
    ordering_fields = ('year',)
