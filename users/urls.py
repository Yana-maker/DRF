from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrievePIView, PaymentUpdatePIView, \
    PaymentDestroyPIView, UserCreateAPIView, UserRetrievePIView, UserUpdatePIView, UserDestroyPIView

app_name = UsersConfig.name

urlpatterns = [
    path('Payment/create/', PaymentCreateAPIView.as_view(), name='Payment-create'),
    path('Payment/', PaymentListAPIView.as_view(), name='Payment-list'),
    path('Payment/Retrieve/<int:pk>/', PaymentRetrievePIView.as_view(), name='Payment-Retrieve'),
    path('Payment/Update/<int:pk>/', PaymentUpdatePIView.as_view(), name='Payment-Update'),
    path('Payment/Destroy/<int:pk>/', PaymentDestroyPIView.as_view(), name='Payment-Destroy'),
    path('User/create/', UserCreateAPIView.as_view(), name='User-create'),
    path('User/Retrieve/<int:pk>/', UserRetrievePIView.as_view(), name='User-Retrieve'),
    path('User/Update/<int:pk>/', UserUpdatePIView.as_view(), name='User-Update'),
    path('User/Destroy/<int:pk>/', UserDestroyPIView.as_view(), name='User-Destroy'),

    # jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token-Obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-Refresh'),
]
