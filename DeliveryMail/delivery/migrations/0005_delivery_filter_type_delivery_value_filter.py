# Generated by Django 4.0.3 on 2022-08-07 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_remove_delivery_message_remove_message_mes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='filter_type',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery',
            name='value_filter',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
