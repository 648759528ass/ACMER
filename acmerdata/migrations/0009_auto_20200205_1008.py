# Generated by Django 3.0.2 on 2020-02-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acmerdata', '0008_auto_20200205_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addstudentqueue',
            name='execution_time',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]