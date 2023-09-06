# Generated by Django 4.1.7 on 2023-08-07 10:35

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('is_enquiry', models.BooleanField(default=False, verbose_name='Is enquiry')),
                ('is_account', models.BooleanField(default=False, verbose_name='Is account')),
                ('is_it', models.BooleanField(default=False, verbose_name='Is it')),
                ('is_hr', models.BooleanField(default=False, verbose_name='Is hr')),
                ('is_training', models.BooleanField(default=False, verbose_name='Is training')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cource_name', models.CharField(max_length=100, null=True)),
                ('fees', models.BigIntegerField()),
                ('durations', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('dob', models.DateField(blank=True, null=True)),
                ('massage', models.TextField(blank=True, null=True)),
                ('whatsapp', models.IntegerField(blank=True, null=True)),
                ('alternate', models.IntegerField(blank=True, null=True)),
                ('media', models.CharField(max_length=50, null=True)),
                ('qualification', models.CharField(max_length=50)),
                ('skill', models.CharField(max_length=150)),
                ('certificate', models.CharField(max_length=200)),
                ('interest', models.CharField(max_length=200)),
                ('reference', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('mode', models.CharField(blank=True, max_length=50, null=True)),
                ('enquiry_Status', models.TextField(choices=[('Finalized', 'Finalized'), ('Pending', 'Pending'), ('Informed_On_whatsapp', 'Informed_On_whatsapp')], default='Pending', max_length=100, null=True)),
                ('Cource_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emanage.cource')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enquiry', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]