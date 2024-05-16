# Generated by Django 3.2.6 on 2021-08-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tram', '0006_auto_20210618_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentprocessingjob',
            name='message',
            field=models.CharField(default='', max_length=16384),
        ),
        migrations.AddField(
            model_name='documentprocessingjob',
            name='status',
            field=models.CharField(choices=[('queued', 'Queued'), ('error', 'Error')], default='queued', max_length=255),
        ),
    ]
