# Generated by Django 3.1.4 on 2021-04-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a club name', max_length=30)),
                ('secy_name', models.CharField(help_text='Enter a secy name', max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]