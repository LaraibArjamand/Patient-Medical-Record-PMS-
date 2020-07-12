# Generated by Django 2.2.3 on 2019-12-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0005_auto_20191206_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=250)),
                ('email', models.EmailField(default='none', max_length=254)),
                ('phone', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
