# Generated by Django 4.1.7 on 2023-04-11 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('car_part', models.CharField(choices=[('T', 'Tires'), ('E', 'Engine'), ('I', 'Interior')], default='T', max_length=1)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.driver')),
            ],
        ),
    ]