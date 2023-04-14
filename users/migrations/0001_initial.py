# Generated by Django 4.1 on 2023-04-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kakao_id', models.BigIntegerField()),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
