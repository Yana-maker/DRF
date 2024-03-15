from django.urls import path


from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrievePIView, PaymentUpdatePIView, \
    PaymentDestroyPIView

app_name = UsersConfig.name


urlpatterns = [
    path('Payment/create/', PaymentCreateAPIView.as_view(), name='Payment-create'),
    path('Payment/list/', PaymentListAPIView.as_view(), name='Payment-list'),
    path('Payment/Retrieve/<int:pk>/', PaymentRetrievePIView.as_view(), name='Payment-Retrieve'),
    path('Payment/Update/<int:pk>/', PaymentUpdatePIView.as_view(), name='Payment-Update'),
    path('Payment/Destroy/<int:pk>/', PaymentDestroyPIView.as_view(), name='Payment-Destroy'),
]