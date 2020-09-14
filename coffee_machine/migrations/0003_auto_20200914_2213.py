# Generated by Django 3.1.1 on 2020-09-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_machine', '0002_auto_20200914_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='sku',
        ),
        migrations.AddField(
            model_name='machine',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_types',
            field=models.CharField(choices=[('1', 'base_model'), ('2', 'premium_model'), ('3', 'deluxe_model')], max_length=50),
        ),
        migrations.AlterField(
            model_name='machine',
            name='product_type_machine',
            field=models.CharField(choices=[('CM10', 'COFFEE_MACHINE_LARGE'), ('CM00', 'COFFEE_MACHINE_SMALL'), ('EM00', 'ESPRESSO_MACHINE')], max_length=50),
        ),
    ]