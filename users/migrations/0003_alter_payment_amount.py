# Generated by Django 5.1.4 on 2024-12-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.PositiveIntegerField(verbose_name="Сумма"),
        ),
    ]