from django.db import models

from config import settings

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Car(models.Model):
    """модель машины"""
    title = models.CharField(max_length=150, verbose_name='назваие')
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Moto(models.Model):
    """модель мотоцикла"""
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Milage(models.Model):
    """модель пробега"""
    car = models.ForeignKey(Car, on_delete=models.CASCADE, **NULLABLE, related_name='milage')
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, **NULLABLE, related_name='milage')
    milage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.PositiveSmallIntegerField(verbose_name='год')


    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.year}'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'
