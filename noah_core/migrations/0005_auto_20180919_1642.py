# Generated by Django 2.1.1 on 2018-09-19 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noah_core', '0004_auto_20180919_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusmodel',
            old_name='kind',
            new_name='group',
        ),
    ]
