# Generated by Django 2.1 on 2018-09-07 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180907_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationdetails',
            name='docfile',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='quotationdetails',
            name='filename',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
