# Generated by Django 2.0.2 on 2019-10-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to='images/')),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
