# Generated by Django 2.0.3 on 2018-06-03 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20180522_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('not-specified', 'Not specified'), ('female', 'Female'), ('male', 'Male')], max_length=80, null=True),
        ),
    ]
