# Generated by Django 5.0.4 on 2024-04-25 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_degree_options_alter_exam_managers'),
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='candidate_for',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='main.studyingarea', verbose_name='Кандидат на'),
            preserve_default=False,
        ),
    ]
