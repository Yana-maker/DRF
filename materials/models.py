from django.db import models

from config import settings
from django.core.validators import RegexValidator


# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Lesson(models.Model):
    """модель урока """
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='lesson/', verbose_name='фото', **NULLABLE)
    link = models.TextField(verbose_name='ссылка на видео',
                            validators=[RegexValidator(r'\b[A-Za-z0-9._'
                                                       r'%+-]+@yourtube'
                                                       r'+\.com\b')], **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Course(models.Model):
    """модель курса """
    title = models.CharField(max_length=150, verbose_name='название')
    image = models.ImageField(upload_to='materials/', verbose_name='фото', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    lesson = models.ManyToManyField(Lesson, verbose_name='уроки')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Subscript(models.Model):
    """модель подписки """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', related_name='subscripts')
    is_active_subscript = models.BooleanField(default=True, verbose_name='подписка')

    def __str__(self):
        return f'{self.course} статус подписки: {self.is_active_subscript}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
