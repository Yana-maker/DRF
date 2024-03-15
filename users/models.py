from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

# Create your models here.
NULLABLE = {'null': True, 'blank': True}

payment_method = {
    'наличные': 'наличные',
    'безналичные': 'безналичные',
}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='фото', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)


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


