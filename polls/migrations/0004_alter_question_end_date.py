# Generated by Django 3.2.7 on 2021-10-09 12:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_question_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='ending date'),
        ),
    ]