from rest_framework import serializers

from .models import Payment, Lesson, Course, User
from materials.serializers import LessonSerializer, CourseSerializer



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
