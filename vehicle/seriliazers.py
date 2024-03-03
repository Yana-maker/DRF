from rest_framework import serializers
from vehicle.models import Car, Moto


class CarSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class MotoSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        field = '__all__'
