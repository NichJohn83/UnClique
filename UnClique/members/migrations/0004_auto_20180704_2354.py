# Generated by Django 2.0.6 on 2018-07-04 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_subscribed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='current_match_Email',
            new_name='current_match_email',
        ),
    ]
