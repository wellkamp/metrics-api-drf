# Generated by Django 3.1.7 on 2021-03-27 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pc', '0001_initial'),
        ('metrics', '0002_auto_20210327_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpumetrics',
            name='pc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pcs', to='pc.personalcomputer'),
        ),
    ]
