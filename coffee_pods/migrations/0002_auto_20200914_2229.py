# Generated by Django 3.1.1 on 2020-09-14 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_pods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pods',
            name='sku',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pods',
            name='coffee_flavors',
            field=models.CharField(choices=[('0', 'COFFEE_FLAVOR_VANILLA'), ('1', 'COFFEE_FLAVOR_CARAMEL'), ('2', 'COFFEE_FLAVOR_PSL'), ('3', 'COFFEE_FLAVOR_MOCHA'), ('4', 'COFFEE_FLAVOR_HAZELNUT')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pods',
            name='pack_sizes',
            field=models.CharField(choices=[('1', '1_dozen'), ('3', '3_dozen'), ('5', '5_dozen'), ('7', '7_dozen')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pods',
            name='product_type_pods',
            field=models.CharField(choices=[('CP1', 'COFFEE_POD_LARGE'), ('CP0', 'COFFEE_POD_SMALL'), ('EP0', 'ESPRESSO_POD')], max_length=50),
        ),
    ]
