from django.contrib import admin

from materials.models import Course, Lesson


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_filter = ('title', 'description',)
    search_fields = ('title', 'description',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link',)
    list_filter = ('title', 'description',)
    search_fields = ('title', 'description',)
