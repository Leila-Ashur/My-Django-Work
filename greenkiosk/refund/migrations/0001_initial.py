# Generated by Django 4.2.3 on 2023-07-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.IntegerField()),
                ('refundId', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('reason', models.TextField()),
                ('status', models.CharField(max_length=52)),
                ('requestDate', models.DateTimeField(auto_now_add=True)),
                ('processedDate', models.DateTimeField()),
            ],
        ),
    ]
