# Generated by Django 3.1.7 on 2021-08-27 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='module_numbering_subtitle',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_subtitle_numbering',
            field=models.CharField(default='-', max_length=5),
        ),
    ]