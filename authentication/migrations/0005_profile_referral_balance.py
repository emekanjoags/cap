# Generated by Django 3.0.8 on 2020-08-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_profile_has_referred'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='referral_balance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]