# Generated by Django 4.0.3 on 2022-08-07 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_alter_client_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='mes',
        ),
        migrations.AddField(
            model_name='delivery',
            name='mes',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='message',
            name='delivery',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='delivery.delivery'),
            preserve_default=False,
        ),
    ]
