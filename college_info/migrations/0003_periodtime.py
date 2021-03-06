# Generated by Django 3.0.8 on 2020-09-11 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_info', '0002_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('8:45-9:45', '8:45-9:45'), ('9:45-10:45', '9:45-10:45'), ('11:00-12:00', '11:00-12:00'), ('12:00-1:00', '12:00-1:00'), ('2:00-3:00', '2:00-3:00')], max_length=50)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=20)),
                ('teach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_info.Teaches')),
            ],
        ),
    ]
