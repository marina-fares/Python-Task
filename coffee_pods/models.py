from django.db import models

# Create your models here.

product_type_pod = (
    ('COFFEE_POD_LARGE','COFFEE_POD_LARGE'),
    ('COFFEE_POD_SMALL','COFFEE_POD_SMALL'),
    ('ESPRESSO_POD','ESPRESSO_POD')
)

coffee_flavor = (
    ('COFFEE_FLAVOR_VANILLA','COFFEE_FLAVOR_VANILLA'),
    ('COFFEE_FLAVOR_CARAMEL','COFFEE_FLAVOR_CARAMEL'),
    ('COFFEE_FLAVOR_PSL','COFFEE_FLAVOR_PSL'),
    ('COFFEE_FLAVOR_MOCHA','COFFEE_FLAVOR_MOCHA'),
    ('COFFEE_FLAVOR_HAZELNUT','COFFEE_FLAVOR_HAZELNUT'),
)

pack_size = (
    ('1_dozen','1_dozen'),
    ('3_dozen','3_dozen'),
    ('5_dozen','5_dozen'),
    ('7_dozen','7_dozen'),
)

class Pods(models.Model):
    product_type_pods = models.CharField( max_length=50, choices= product_type_pod)
    coffee_flavors = models.CharField( max_length=50, choices= coffee_flavor)
    pack_sizes = models.CharField( max_length=50, choices= pack_size)
    
