# Generated by Django 3.1 on 2020-09-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_appointment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
    ]