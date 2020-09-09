# Generated by Django 3.1 on 2020-09-09 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_pocketwatch_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('model', models.CharField(max_length=254)),
                ('type', models.CharField(max_length=254)),
                ('date', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Appointments',
            },
        ),
        migrations.RemoveField(
            model_name='appointmenttype',
            name='friendly_name',
        ),
        migrations.DeleteModel(
            name='PocketWatch',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.appointmenttype'),
        ),
    ]
