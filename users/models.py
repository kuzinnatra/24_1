from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from courses.models import Cours, Lesson

class User(AbstractUser):
    usermame = None

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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    PAYMENT_CHOICES = [
        ('BANK_TRANSFER', 'Банковский перевод'),
        ('CASH', 'Наличными'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(default=datetime.now, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Cours, on_delete=models.SET_NULL, verbose_name='Оплаченный курс', blank=True,
                                    null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Оплаченный урок', blank=True,
                                    null=True, )
    amount = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Сумма')
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.user} - {self.amount} ({self.payment_date})"


