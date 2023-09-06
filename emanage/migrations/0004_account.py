# Generated by Django 4.1.7 on 2023-08-08 08:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emanage', '0003_alter_enquiry_certificate_alter_enquiry_interest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_installment', models.IntegerField()),
                ('pay_date', models.DateTimeField(default=datetime.date.today)),
                ('first_installment', models.FloatField(blank=True, null=True)),
                ('payment_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('receipt', models.ImageField(upload_to='media/')),
                ('second_installment', models.FloatField(blank=True, null=True)),
                ('second_date', models.DateField(blank=True, null=True)),
                ('third_installment', models.FloatField(blank=True, null=True)),
                ('third_date', models.DateField(blank=True, null=True)),
                ('four_installment', models.FloatField(blank=True, null=True)),
                ('four_date', models.DateField(blank=True, null=True)),
                ('payment_status', models.TextField(choices=[('Pending', 'Pending'), ('first_installment', 'first_installment'), ('second_installment', 'second_installment'), ('third_installment', 'third_installment'), ('fourth_installment', 'fourth_installment'), ('installment_completed', 'installment_completed')], default='Pending', max_length=100, null=True)),
                ('account_remark', models.CharField(max_length=500, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('amount_date', models.DateField(default=datetime.date.today)),
                ('amount_remaining', models.PositiveIntegerField(blank=True, null=True)),
                ('total_amount', models.FloatField(blank=True, null=True)),
                ('enquiry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.enquiry')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]