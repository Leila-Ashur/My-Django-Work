# Generated by Django 4.2.2 on 2023-06-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payments_status', models.CharField(max_length=32)),
                ('Transation_ID', models.CharField(max_length=10)),
                ('Payment_method', models.CharField(max_length=15)),
            ],
        ),
    ]
