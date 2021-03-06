# Generated by Django 3.0.4 on 2020-04-05 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField(choices=[(1, 'Wrost'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Excellent!')])),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_singer', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.Album')),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.Singer')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.Singer'),
        ),
    ]
