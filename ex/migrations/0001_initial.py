# Generated by Django 3.1.1 on 2020-09-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('birth', models.DateField(verbose_name='생년월일')),
                ('job', models.CharField(max_length=30, verbose_name='직업')),
                ('debut', models.DateField(verbose_name='데뷔')),
                ('level', models.CharField(max_length=30, verbose_name='학력')),
                ('photo', models.ImageField(upload_to='%d')),
                ('refresh', models.IntegerField(default=0, verbose_name='접속횟수')),
            ],
            options={
                'verbose_name_plural': 'star',
            },
        ),
    ]
