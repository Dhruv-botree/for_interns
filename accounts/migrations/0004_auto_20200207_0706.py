# Generated by Django 3.0.3 on 2020-02-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200207_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='facilities',
            field=models.ManyToManyField(related_name='facilities', to='accounts.Facility'),
        ),
    ]