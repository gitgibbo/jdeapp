# Generated by Django 4.0.1 on 2022-01-29 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bos', '0006_bos_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bos',
            name='id',
        ),
        migrations.AddField(
            model_name='bos',
            name='BOS_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
