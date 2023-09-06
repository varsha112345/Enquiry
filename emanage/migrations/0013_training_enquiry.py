# Generated by Django 4.1.7 on 2023-08-31 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emanage', '0012_reason_for_follow_up_enroll_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training_Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('course', models.CharField(max_length=200)),
                ('durations', models.CharField(max_length=50, null=True)),
                ('interest', models.CharField(max_length=200)),
            ],
        ),
    ]