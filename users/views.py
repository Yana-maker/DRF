from django.shortcuts import render
from rest_framework import generics

from users.models import Payment
from users.serializers import PaymentSerializer


# Create your views here.
class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentRetrievePIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentUpdatePIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()


