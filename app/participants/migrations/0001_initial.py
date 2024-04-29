# Generated by Django 5.0.4 on 2024-04-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Імя')),
                ('lastname', models.CharField(max_length=50, verbose_name='Прізвище')),
                ('surname', models.CharField(max_length=50, verbose_name='По батькові')),
                ('email', models.EmailField(max_length=254, verbose_name='Електронна пошта')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефону')),
            ],
        ),
    ]