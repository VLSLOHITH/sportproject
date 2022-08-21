# Generated by Django 3.1.5 on 2021-05-07 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0005_auto_20210506_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='general_equipname',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sportapp.generalequipment'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='equipment_name',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sportapp.equipment'),
        ),
    ]