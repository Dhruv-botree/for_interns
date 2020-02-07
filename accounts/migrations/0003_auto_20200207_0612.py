# Generated by Django 3.0.3 on 2020-02-07 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200206_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='house',
            name='facilities',
            field=models.ManyToManyField(related_name='facilitie', to='accounts.Facility'),
        ),
    ]
