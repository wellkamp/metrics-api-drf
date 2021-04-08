# Generated by Django 3.1.7 on 2021-04-07 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalComputer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainboard', models.CharField(max_length=50)),
                ('gpu', models.CharField(max_length=50)),
                ('processador', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'personal_computer',
                'verbose_name_plural': 'personal_computers',
            },
        ),
        migrations.CreateModel(
            name='MemoryMetrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used', models.CharField(max_length=50)),
                ('available', models.CharField(max_length=50)),
                ('created_at', models.DateField()),
                ('hour_at', models.TimeField()),
                ('pc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory_temps', to='personalmetrics.personalcomputer')),
            ],
            options={
                'verbose_name': 'memory_metric',
                'verbose_name_plural': 'memory_metrics',
            },
        ),
        migrations.CreateModel(
            name='GPUMetrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpu_core', models.CharField(max_length=50)),
                ('gpu_memory', models.CharField(max_length=50)),
                ('gpu_vrm_core', models.CharField(max_length=50)),
                ('gpu_hot_spot', models.CharField(max_length=50)),
                ('created_at', models.DateField()),
                ('hour_at', models.TimeField()),
                ('pc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpu_temps', to='personalmetrics.personalcomputer')),
            ],
            options={
                'verbose_name': 'gpu_metric',
                'verbose_name_plural': 'gpu_metrics',
            },
        ),
    ]