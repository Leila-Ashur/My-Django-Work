# Generated by Django 4.2.2 on 2023-06-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField()),
                ('comments', models.TextField()),
                ('name', models.CharField(max_length=32)),
                ('date', models.DateField()),
            ],
        ),
    ]
