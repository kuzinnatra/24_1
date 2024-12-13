# Generated by Django 5.1.4 on 2024-12-13 11:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_alter_lesson_cours"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="cours",
            field=models.ForeignKey(
                help_text="Выберите курс",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to="courses.cours",
                verbose_name="Курс",
            ),
        ),
    ]
