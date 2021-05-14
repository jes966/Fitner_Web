# Generated by Django 3.1.7 on 2021-05-13 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnerapp', '0002_ranking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10, verbose_name='순서')),
                ('high', models.CharField(max_length=10, verbose_name='최고 유사도')),
                ('low', models.CharField(max_length=10, verbose_name='최저 유사도')),
                ('average', models.CharField(max_length=10, verbose_name='평균 유사도')),
                ('high_img_route', models.CharField(max_length=256, verbose_name='최고 유사도 이미지 경로')),
                ('low_img_route', models.CharField(max_length=256, verbose_name='최저 유사도 이미지 경로')),
                ('high_start_section', models.CharField(max_length=64, verbose_name='최고 유사도 영상 시작 구간')),
                ('high_end_section', models.CharField(max_length=64, verbose_name='최고 유사도 영상 끝 구간')),
                ('low_start_section', models.CharField(max_length=64, verbose_name='최저 유사도 영상 시작 구간')),
                ('low_end_section', models.CharField(max_length=64, verbose_name='최저 유사도 영상 끝 구간')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'db_table': 'statistics',
            },
        ),
    ]
