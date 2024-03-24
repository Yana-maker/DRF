from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscript
from materials.paginators import Material_pagination
from materials.serializers import CourseSerializer, LessonSerializer, SubscriptSerializer
from users.permissions import IsOwner, IsModerator, IsNotModerator


# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    """viewset для модели курс"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = Material_pagination
    permission_classes_by_action = {'create': [IsAuthenticated, IsNotModerator],
                                    'list': [IsAuthenticated, IsOwner | IsModerator],
                                    'retrieve': [IsAuthenticated, IsOwner | IsModerator],
                                    'update': [IsAuthenticated, IsOwner | IsModerator],
                                    'destroy': [IsAuthenticated, IsOwner, IsNotModerator],
                                    }

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def create(self, request, *args, **kwargs):
        return super(CourseViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(CourseViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(CourseViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(CourseViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(CourseViewSet, self).destroy(request, *args, **kwargs)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    """создание урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsNotModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """список уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    pagination_class = Material_pagination


class LessonRetrievePIView(generics.RetrieveAPIView):
    """просмотр деталей урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonUpdatePIView(generics.UpdateAPIView):
    """редактирование урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonDestroyPIView(generics.DestroyAPIView):
    """удаление урока"""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner, IsNotModerator]


class CourseSubscriptView(APIView):
    """подписка на курс"""
    serializer_class = SubscriptSerializer
    queryset = Subscript.objects.all()


    def post(self):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscript.objects.filter(user=user, course=course_item)
        print(self.request.data.get("course"))
        print(user)
        print(subs_item)


        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'

        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            subs_item = Subscript.objects.create(user=user, course=course_item)
            subs_item.save()
            message = 'подписка добавлена'
        # Возвращаем ответ в API
        return Response({'message': message})
