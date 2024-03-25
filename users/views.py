from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from users.models import Payment, User
from users.permissions import IsOwner, IsModerator, IsNotModerator
from users.serializers import PaymentSerializer, UserSerializer


# Create your views here.


class UserCreateAPIView(generics.CreateAPIView):
    """создание юзера"""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.owner = self.request.user
        new_user.save()


class UserRetrievePIView(generics.RetrieveAPIView):
    """просмотр деталей юзера"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class UserUpdatePIView(generics.UpdateAPIView):
    """редактирование юзера"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class UserDestroyPIView(generics.DestroyAPIView):
    """удаление юзера"""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner, IsNotModerator]


class PaymentCreateAPIView(generics.CreateAPIView):
    """создание платежа"""
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsOwner, IsNotModerator]


class PaymentListAPIView(generics.ListAPIView):
    """список всех созданных платежей"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('payment_date',)



class PaymentRetrievePIView(generics.RetrieveAPIView):
    """просмотр деталей платежа"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentUpdatePIView(generics.UpdateAPIView):
    """редактирование платежа"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentDestroyPIView(generics.DestroyAPIView):
    """удаление платежа"""
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsOwner, IsNotModerator]
