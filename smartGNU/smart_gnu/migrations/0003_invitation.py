# Generated by Django 3.0.2 on 2020-03-01 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_gnu', '0002_collegeuser_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('user_type', models.IntegerField(blank=True, choices=[(0, 'user'), (1, 'Admin'), (2, 'Super Admin')], null=True)),
            ],
        ),
    ]