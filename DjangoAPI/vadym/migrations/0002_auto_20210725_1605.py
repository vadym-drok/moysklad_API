# Generated by Django 2.1.15 on 2021-07-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vadym', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sum',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=12, null=True),
        ),
    ]