from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrievePIView, \
    LessonUpdatePIView, LessonDestroyPIView, CourseSubscriptView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('Lesson/create/', LessonCreateAPIView.as_view(), name='Lesson-create'),
    path('Lesson/list/', LessonListAPIView.as_view(), name='Lesson-list'),
    path('Lesson/Retrieve/<int:pk>/', LessonRetrievePIView.as_view(), name='Lesson-Retrieve'),
    path('Lesson/Update/<int:pk>/', LessonUpdatePIView.as_view(), name='Lesson-Update'),
    path('Lesson/Destroy/<int:pk>/', LessonDestroyPIView.as_view(), name='Lesson-Destroy'),
    path('Subscript/', CourseSubscriptView.as_view(), name='Subscript')
] + router.urls
