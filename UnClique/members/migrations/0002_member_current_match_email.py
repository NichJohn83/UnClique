# Generated by Django 2.0.6 on 2018-07-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='current_match_Email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
