# Generated by Django 2.0.3 on 2018-03-12 13:37

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0008_auto_20180311_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]
