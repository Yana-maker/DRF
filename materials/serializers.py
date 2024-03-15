from rest_framework import serializers

from materials.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, course):
        if Lesson.objects.filter(course=course).count():
            return Lesson.objects.filter(course=course).count()
        return 0

