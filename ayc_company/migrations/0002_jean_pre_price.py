# Generated by Django 3.2.5 on 2021-07-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayc_company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jean',
            name='pre_price',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]