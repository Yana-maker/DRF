from rest_framework import serializers

from .models import Payment, Lesson, Course
from materials.serializers import LessonSerializer, CourseSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
