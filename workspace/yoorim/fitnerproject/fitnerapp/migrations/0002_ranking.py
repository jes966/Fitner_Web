# Generated by Django 3.1.7 on 2021-05-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, verbose_name='이름')),
                ('userphone', models.CharField(max_length=11, verbose_name='전화번호')),
                ('similarity', models.CharField(max_length=10, verbose_name='유사도')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'db_table': 'ranking',
            },
        ),
    ]