from rest_framework import serializers

from materials.models import Lesson, Course, Subscript


class LessonSerializer(serializers.ModelSerializer):
    """сериализатор для урока"""
    class Meta:
        model = Lesson
        fields = '__all__'


class SubscriptSerializer(serializers.ModelSerializer):
    """сериализатор для подписки"""
    class Meta:
        model = Subscript
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """сериализатор для курса"""
    subscript = SubscriptSerializer(read_only=True)
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, course):
        """подсчет кол-ва уроков в одном курсе"""
        if Lesson.objects.filter(course=course).count():
            return Lesson.objects.filter(course=course).count()
        return 0



