# Generated by Django 4.1.1 on 2022-10-03 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/default_profile.png', null=True, upload_to='profiles/'),
        ),
    ]
