# Generated by Django 4.0.6 on 2022-07-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0005_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Profile_pic',
            field=models.ImageField(blank=True, upload_to='pro_ managepic'),
        ),
    ]