# Generated by Django 3.0.2 on 2020-03-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_gnu', '0004_auto_20200303_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeMCU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_mcu_name', models.CharField(blank=True, max_length=255, null=True)),
                ('node_mcu_ip', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]