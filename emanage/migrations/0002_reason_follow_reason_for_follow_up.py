# Generated by Django 4.1.7 on 2023-08-07 10:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emanage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reason_follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='reason_for_follow_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField(auto_now=True)),
                ('remark', models.CharField(max_length=100, null=True)),
                ('Followup_Status', models.TextField(choices=[('FollowUp Done', 'FollowUp Done'), ('Pending', 'Pending')], default='Pending', max_length=100, null=True)),
                ('enquiry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.enquiry')),
                ('reason', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.reason_follow')),
            ],
        ),
    ]
