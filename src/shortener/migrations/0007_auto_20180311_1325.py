# Generated by Django 2.0.3 on 2018-03-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0006_auto_20180310_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
