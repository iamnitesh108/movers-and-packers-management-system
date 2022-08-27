# Generated by Django 4.0.4 on 2022-05-23 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('emailid', models.CharField(max_length=100, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=200, null=True)),
                ('mdate', models.DateField(null=True)),
                ('isread', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=5000, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('shiftingloc', models.CharField(max_length=200, null=True)),
                ('briefitems', models.CharField(max_length=100, null=True)),
                ('items', models.CharField(max_length=5000, null=True)),
                ('professional', models.CharField(max_length=200, null=True)),
                ('requestdate', models.DateField(null=True)),
                ('remark', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('updationdate', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
