from django.urls import path


from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrievePIView, PaymentUpdatePIView, \
    PaymentDestroyPIView, UserCreateAPIView, UserListAPIView, UserRetrievePIView, UserUpdatePIView, UserDestroyPIView

app_name = UsersConfig.name


urlpatterns = [
    path('Payment/create/', PaymentCreateAPIView.as_view(), name='Payment-create'),
    path('Payment/', PaymentListAPIView.as_view(), name='Payment-list'),
    path('Payment/Retrieve/<int:pk>/', PaymentRetrievePIView.as_view(), name='Payment-Retrieve'),
    path('Payment/Update/<int:pk>/', PaymentUpdatePIView.as_view(), name='Payment-Update'),
    path('Payment/Destroy/<int:pk>/', PaymentDestroyPIView.as_view(), name='Payment-Destroy'),
    path('User/create/', UserCreateAPIView.as_view(), name='User-create'),
    path('User/list/', UserListAPIView.as_view(), name='User-list'),
    path('User/Retrieve/<int:pk>/', UserRetrievePIView.as_view(), name='User-Retrieve'),
    path('User/Update/<int:pk>/', UserUpdatePIView.as_view(), name='User-Update'),
    path('User/Destroy/<int:pk>/', UserDestroyPIView.as_view(), name='User-Destroy'),
]