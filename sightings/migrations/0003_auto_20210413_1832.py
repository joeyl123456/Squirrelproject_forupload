# Generated by Django 3.2 on 2021-04-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_auto_20210411_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sight',
            name='Approaches',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Chasing',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Climbing',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Eating',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Foraging',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Indifferent',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Kuks',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Moans',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Other_Activities',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Quaas',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Running',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Runs_From',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Tail_Flags',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Tail_Twitches',
            field=models.BooleanField(null=True),
        ),
    ]
