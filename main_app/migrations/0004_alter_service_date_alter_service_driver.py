# Generated by Django 4.1.7 on 2023-04-11 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateField(verbose_name='service_date'),
        ),
        migrations.AlterField(
            model_name='service',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car'),
        ),
    ]
