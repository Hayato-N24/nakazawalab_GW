# Generated by Django 3.2.4 on 2021-07-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=200)),
                ('allergy', models.CharField(max_length=200, null=True)),
                ('like', models.CharField(max_length=200, null=True)),
                ('dislike', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
