# Generated by Django 2.2.12 on 2020-04-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200419_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='raiting',
            new_name='rait',
        ),
        migrations.AddField(
            model_name='skill',
            name='status',
            field=models.CharField(default='learn', max_length=30),
        ),
    ]