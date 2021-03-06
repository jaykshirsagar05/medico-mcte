# Generated by Django 3.0.5 on 2020-08-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armyno', models.CharField(max_length=15)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('posttype', models.CharField(max_length=20)),
                ('relation', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('rank', models.TextField(max_length=20)),
                ('healthproblem', models.TextField(max_length=100)),
                ('problemhistory', models.TextField(max_length=100)),
            ],
        ),
    ]
