# Generated by Django 5.1.4 on 2024-12-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_payment_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты"),
        ),
    ]
