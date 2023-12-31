# Generated by Django 4.2.5 on 2023-10-16 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airlane', '0001_initial'),
        ('plane', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fro', models.CharField(max_length=260)),
                ('to', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airlane.airline')),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plane.plane')),
            ],
        ),
    ]
