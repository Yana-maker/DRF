from rest_framework import serializers
from vehicle.models import Car, Moto, Milage


class MilageSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = '__all__'


class CarSeriliazer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage.all.first.milage', read_only=True)
    milage = MilageSeriliazer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'


class MotoSeriliazer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, instance):
        if instance.milage.all().first().milage:
            return instance.milage.all().first().milage
        return 0


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSeriliazer()

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto')



class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSeriliazer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'

    def create(self, validated_data):
        milage = validated_data.pop('milage')

        moto_item = Moto.objects.create(**validated_data)
        for m in milage:
            Milage.objects.create(**m, moto=moto_item)

        return moto_item
