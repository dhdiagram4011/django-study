# Generated by Django 2.2.1 on 2019-11-22 00:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rev_post',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
