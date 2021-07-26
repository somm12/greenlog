# Generated by Django 3.2.4 on 2021-07-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kinds', models.CharField(default='', max_length=7)),
                ('title', models.CharField(default='', max_length=30, null=True)),
                ('writer', models.CharField(default='', max_length=10)),
                ('content', models.TextField(default='', null=True)),
                ('image', models.ImageField(null=True, upload_to=None)),
                ('date', models.DateTimeField(default='', null=True)),
                ('firstPlace', models.CharField(default='', max_length=30, null=True)),
                ('like', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(default='', max_length=10)),
                ('nickname', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(default='', max_length=20)),
                ('profile', models.ImageField(upload_to=None)),
                ('Member', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
