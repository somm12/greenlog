# Generated by Django 3.2.6 on 2021-08-13 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(default='', max_length=10)),
                ('nickname', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(default='', max_length=100)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Member', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kinds', models.CharField(default='', max_length=7)),
                ('title', models.CharField(default='', max_length=30, null=True)),
                ('writer', models.CharField(default='', max_length=10)),
                ('content', models.TextField(default='', null=True)),
                ('date', models.DateTimeField(default='', null=True)),
                ('firstPlace', models.CharField(default='', max_length=30, null=True)),
                ('like', models.IntegerField(default=0, null=True)),
                ('like_users', models.ManyToManyField(to='log.User')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='log.post')),
            ],
        ),
    ]
