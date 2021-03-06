# Generated by Django 3.0.3 on 2020-02-25 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='web_class',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=20, unique=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('uptime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='web_class_obj',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('obj_name', models.CharField(max_length=40, unique=True)),
                ('obj_environment', models.IntegerField(choices=[(1, '生产环境'), (2, '测试环境')], default=1)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('uptime', models.DateTimeField(auto_now=True, null=True)),
                ('web_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site_navigation.web_class')),
            ],
        ),
        migrations.CreateModel(
            name='web_site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=26, unique=True)),
                ('site_url', models.CharField(max_length=255, unique=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('uptime', models.DateTimeField(auto_now=True, null=True)),
                ('web_class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site_navigation.web_class_obj')),
            ],
        ),
    ]
