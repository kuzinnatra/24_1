from django.db import models


class Cours(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите низвание курса",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание курса", help_text="Опишите курс"
    )
    photo = models.ImageField(
        upload_to="lesson/photo",
        verbose_name="Картинка",
        help_text="Загрузите картинку",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите низвание урока",
    )
    cours = models.ForeignKey(
        Cours, on_delete=models.CASCADE, verbose_name="Курс", help_text="Выберите курс"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание урока", help_text="Опишите урок"
    )
    photo = models.ImageField(
        upload_to="lesson/photo",
        verbose_name="Картинка",
        help_text="Загрузите картинку",
        blank=True,
        null=True,
    )
    video_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Cсылка на видео",
        help_text="Вставьте ссылку на видео урока",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
