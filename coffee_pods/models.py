from django.db import models
from django.utils.text import slugify

# Create your models here.

product_type_pod = (
    ('CP1','COFFEE_POD_LARGE'),
    ('CP0','COFFEE_POD_SMALL'),
    ('EP0','ESPRESSO_POD')
)

coffee_flavor = (
    ('0','COFFEE_FLAVOR_VANILLA'),
    ('1','COFFEE_FLAVOR_CARAMEL'),
    ('2','COFFEE_FLAVOR_PSL'),
    ('3','COFFEE_FLAVOR_MOCHA'),
    ('4','COFFEE_FLAVOR_HAZELNUT'),
)

pack_size = (
    ('1','1_dozen'),
    ('3','3_dozen'),
    ('5','5_dozen'),
    ('7','7_dozen'),
)

class Pods(models.Model):
    product_type_pods = models.CharField( max_length=50, choices= product_type_pod)
    coffee_flavors = models.CharField( max_length=50, choices= coffee_flavor)
    pack_sizes = models.CharField( max_length=50, choices= pack_size)
    sku = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.sku = ''.join((slugify(self.product_type_pods), slugify(self.coffee_flavors), slugify(self.pack_sizes)))
        super(Pods, self).save(*args, **kwargs)


    def __str__(self):
        return self.sku
    
