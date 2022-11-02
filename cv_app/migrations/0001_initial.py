# Generated by Django 3.2.16 on 2022-11-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('KOTTAYAM', 'KOTTAYAM'), ('THRISHUR', 'THRISHUR'), ('ERANAKULAM', 'ERANAKULAM')], max_length=50)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('piimage', models.ImageField(blank=True, upload_to='pimages')),
                ('docfile', models.FileField(blank=True, upload_to='docfiles')),
            ],
        ),
    ]