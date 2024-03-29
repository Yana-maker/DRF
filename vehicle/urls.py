from django.urls import path
from rest_framework.routers import DefaultRouter

from vehicle.apps import VehicleConfig
from vehicle.views import CarViewSet, MotoCreateAPIView, MotoListAPIView, MotoRetrievePIView, MotoUpdatePIView, \
    MotoDestroyPIView, MilageCreateAPIView, MotoMilageListAPIView, MilageListAPIView

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'car', CarViewSet, basename='car')

urlpatterns = [
    path('moto/create/', MotoCreateAPIView.as_view(), name='moto-create'),
    path('moto/list/', MotoListAPIView.as_view(), name='moto-list'),
    path('moto/Retrieve/<int:pk>/', MotoRetrievePIView.as_view(), name='moto-Retrieve'),
    path('moto/Update/<int:pk>/', MotoUpdatePIView.as_view(), name='moto-Update'),
    path('moto/Destroy/<int:pk>/', MotoDestroyPIView.as_view(), name='moto-Destroy'),
    path('milage/create/', MilageCreateAPIView.as_view(), name='milage-create'),
    path('moto/milage/', MotoMilageListAPIView.as_view(), name='moto-milage'),
    path('milage/', MilageListAPIView.as_view(), name='milage')
] + router.urls
