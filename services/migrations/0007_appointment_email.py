# Generated by Django 3.1 on 2020-09-16 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20200915_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(blank=True, max_length=70),
        ),
    ]