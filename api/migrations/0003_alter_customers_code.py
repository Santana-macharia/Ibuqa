# Generated by Django 3.2.13 on 2022-06-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_customers_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='code',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
