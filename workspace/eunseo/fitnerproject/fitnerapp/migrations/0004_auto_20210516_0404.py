# Generated by Django 3.1.7 on 2021-05-16 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnerapp', '0003_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='average',
            field=models.FloatField(max_length=10, verbose_name='평균 유사도'),
        ),
        migrations.AlterField(
            model_name='data',
            name='high',
            field=models.FloatField(max_length=10, verbose_name='최고 유사도'),
        ),
        migrations.AlterField(
            model_name='data',
            name='high_end_section',
            field=models.IntegerField(max_length=64, verbose_name='최고 유사도 영상 끝 구간'),
        ),
        migrations.AlterField(
            model_name='data',
            name='high_start_section',
            field=models.IntegerField(max_length=64, verbose_name='최고 유사도 영상 시작 구간'),
        ),
        migrations.AlterField(
            model_name='data',
            name='low',
            field=models.FloatField(max_length=10, verbose_name='최저 유사도'),
        ),
        migrations.AlterField(
            model_name='data',
            name='low_end_section',
            field=models.IntegerField(max_length=64, verbose_name='최저 유사도 영상 끝 구간'),
        ),
        migrations.AlterField(
            model_name='data',
            name='low_start_section',
            field=models.IntegerField(max_length=64, verbose_name='최저 유사도 영상 시작 구간'),
        ),
        migrations.AlterField(
            model_name='data',
            name='total_time',
            field=models.IntegerField(max_length=64, verbose_name='운동시간'),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='similarity',
            field=models.FloatField(max_length=256, verbose_name='유사도'),
        ),
    ]
