# Generated by Django 4.1.7 on 2023-08-08 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emanage', '0005_enquiry_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='alternate',
            new_name='Alternate_Number',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='certificate',
            new_name='Area_of_Intrest',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='interest',
            new_name='Certification_Done',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='mobile',
            new_name='Contact_Number',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='dob',
            new_name='Date_of_Birth',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='email',
            new_name='Email_Address',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='name',
            new_name='Full_Name',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='media',
            new_name='How_did_you_hear_about_us',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='mode',
            new_name='Office_Location_Preference',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='Address',
            new_name='Permanent_Address',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='skill',
            new_name='Technical_Skills',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='whatsapp',
            new_name='Whatsapp_Number',
        ),
    ]
