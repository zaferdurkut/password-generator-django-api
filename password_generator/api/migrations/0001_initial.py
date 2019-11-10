# Generated by Django 2.2.7 on 2019-11-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.NullBooleanField()),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
