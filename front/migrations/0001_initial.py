# Generated by Django 2.2 on 2020-04-11 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_id', models.CharField(max_length=10, unique=True)),
                ('vender', models.CharField(max_length=50)),
                ('mac_type', models.CharField(max_length=50)),
                ('model_id', models.CharField(blank=True, max_length=50)),
                ('mac_sn', models.CharField(max_length=50)),
                ('use_des', models.TextField(blank=True)),
                ('location', models.CharField(max_length=50)),
                ('ipmi', models.GenericIPAddressField(protocol='ipv4')),
                ('level', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'machine',
                'ordering': ['mac_id'],
            },
        ),
        migrations.CreateModel(
            name='OpsLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ops_obj', models.CharField(max_length=50)),
                ('ops_subject', models.CharField(max_length=200)),
                ('ops_log', models.TextField()),
                ('des', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'OpsLog',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('problem_des', models.TextField()),
                ('solution', models.TextField()),
                ('results', models.BooleanField(default=True)),
                ('new_pn', models.CharField(max_length=20)),
                ('new_sn', models.CharField(max_length=20)),
                ('old_pn', models.CharField(max_length=20)),
                ('old_sn', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('mac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.Machine')),
            ],
            options={
                'db_table': 'Maintenance',
                'ordering': ['date'],
            },
        ),
    ]
