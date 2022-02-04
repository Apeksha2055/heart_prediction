# Generated by Django 3.0.2 on 2021-11-18 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='fbs',
            field=models.BooleanField(choices=[(1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='oldpeak',
            field=models.FloatField(choices=[(1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='sex',
            field=models.BooleanField(choices=[(1, 'Male'), (0, 'Femele')]),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='target',
            field=models.BooleanField(choices=[(1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='trestps',
            field=models.BooleanField(choices=[(1, 'Yes'), (0, 'No')]),
        ),
    ]