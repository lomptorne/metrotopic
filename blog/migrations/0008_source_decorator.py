# Generated by Django 3.0.6 on 2020-06-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200605_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='decorator',
            field=models.CharField(default='link', max_length=200),
            preserve_default=False,
        ),
    ]
