from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings
from materials.models import Course, Lesson
from django.utils.translation import gettext_lazy as _



# Create your models here.
NULLABLE = {'null': True, 'blank': True}


payment_method = {
    'наличные': 'наличные',
    'безналичные': 'безналичные',
}


class UserRole(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    role = models.CharField(max_length=9, choices=UserRole.choices, default=UserRole.MEMBER)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateTimeField(verbose_name='дата платежа')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок')
    payment_method = models.TextField(choices=payment_method, verbose_name='способ оплаты')
    amount_payment = models.IntegerField(verbose_name='сумма платежа')

    def __str__(self):
        return f"{self.payment_date}"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


