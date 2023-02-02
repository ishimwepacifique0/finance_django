# Generated by Django 4.1.1 on 2023-01-03 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addemployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('phonenumber', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('joineddate', models.DateTimeField(auto_now_add=True)),
                ('salary', models.IntegerField(default=0)),
                ('assurance', models.CharField(max_length=255)),
                ('bankaccountno', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=255)),
                ('phonenumber', models.IntegerField()),
                ('savedby', models.CharField(max_length=255)),
                ('last_update_by', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart_name', models.CharField(max_length=255)),
                ('phonenumber', models.IntegerField()),
                ('savedby', models.CharField(max_length=255)),
                ('last_update_by', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(max_length=255)),
                ('sender', models.CharField(max_length=255)),
                ('receiver', models.CharField(max_length=255)),
                ('datetime', models.DateField(default=datetime.date(2023, 1, 3))),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.IntegerField()),
                ('payment_date', models.DateField()),
                ('payment_period', models.IntegerField()),
                ('last_payment_by', models.CharField(max_length=255)),
            ],
        ),
    ]
