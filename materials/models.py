from django.db import models

from config import settings

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='lesson/', verbose_name='фото', **NULLABLE)
    link = models.TextField(verbose_name='ссылка на видео', **NULLABLE)
    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    image = models.ImageField(upload_to='materials/', verbose_name='фото', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    lesson = models.ManyToManyField(Lesson, verbose_name='уроки')
    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
