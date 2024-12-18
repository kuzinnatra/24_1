from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from courses.models import Cours, Lesson

class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    PAYMENT_CHOICES = [
        ('BANK_TRANSFER', 'Банковский перевод'),
        ('CASH', 'Наличными'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Cours, on_delete=models.SET_NULL, verbose_name='Оплаченный курс', blank=True,
                                    null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Оплаченный урок', blank=True,
                                    null=True, )
    amount = models.PositiveIntegerField(verbose_name='Сумма платежа', help_text='Укажите сумму платежа')
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')
    session_id = models.CharField(max_length=255, verbose_name='Id сессии', blank=True, null=True)
    link = models.URLField(max_length=400, verbose_name='Cсылка на оплату', blank=True, null=True)
    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.user} - {self.amount} ({self.payment_date})"


