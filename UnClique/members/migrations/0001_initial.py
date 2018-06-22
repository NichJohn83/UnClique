# Generated by Django 2.0.6 on 2018-06-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('preferred_name', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=30)),
                ('classification', models.CharField(choices=[('first', 'First Year'), ('second', 'Second Year'), ('third', 'Third Year'), ('fourth', 'Fourth Year'), ('fifth+', 'Fifth Year or higher'), ('grad', 'Graduate Student'), ('faculty', 'Faculty'), ('staff', 'Staff')], default='first', max_length=10)),
            ],
        ),
    ]