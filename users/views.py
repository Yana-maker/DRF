from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from users.models import Payment
from users.serializers import PaymentSerializer, UserSerializer


# Create your views here.
class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('payment_date',)


class PaymentRetrievePIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentUpdatePIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()


# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = Payment.objects.all()



class UserRetrievePIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = Payment.objects.all()


class UserUpdatePIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = Payment.objects.all()


class UserDestroyPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
