# Generated by Django 4.1.7 on 2023-08-10 11:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emanage', '0007_remove_enquiry_location_enquiry_training_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(blank=True, max_length=500, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.category')),
                ('enquiry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.enquiry')),
            ],
        ),
        migrations.CreateModel(
            name='system_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('model_name', models.CharField(blank=True, max_length=500, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=50, null=True)),
                ('desktop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.desktop')),
            ],
        ),
        migrations.CreateModel(
            name='Assert_create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(blank=True, max_length=50, null=True)),
                ('a_description', models.TextField(blank=True, max_length=500, null=True)),
                ('make_year', models.CharField(max_length=50)),
                ('model_name', models.CharField(blank=True, max_length=500, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=50, null=True)),
                ('condition', models.CharField(blank=True, max_length=10, null=True)),
                ('system', models.CharField(blank=True, max_length=10, null=True)),
                ('asset_photo', models.ImageField(upload_to='media/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.category')),
            ],
        ),
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('model_name', models.CharField(blank=True, max_length=500, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=50, null=True)),
                ('L_condition', models.CharField(blank=True, max_length=10, null=True)),
                ('L_purpose', models.CharField(blank=True, max_length=200, null=True)),
                ('L_allocation_date', models.DateField(default=datetime.date.today)),
                ('L_photos', models.ImageField(upload_to='media/')),
                ('system_status', models.TextField(choices=[('allocated', 'allocated'), ('not_allocated', 'not_allocated'), ('scrap', 'scrap')], default='not_allocated', max_length=100, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.category')),
                ('desktop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.desktop')),
                ('enquiry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.enquiry')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='it', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
