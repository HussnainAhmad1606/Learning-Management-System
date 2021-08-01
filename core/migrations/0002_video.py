# Generated by Django 3.1.4 on 2021-08-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_name', models.CharField(max_length=50)),
                ('video_description', models.CharField(max_length=200)),
                ('video_embed_code', models.CharField(max_length=300)),
                ('video_category', models.ManyToManyField(to='core.Course')),
            ],
        ),
    ]