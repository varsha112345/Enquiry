# Generated by Django 4.1.7 on 2023-08-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emanage', '0011_alter_account_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='reason_for_follow_up',
            name='Enroll_flag',
            field=models.BooleanField(default=False),
        ),
    ]