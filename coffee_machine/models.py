from django.db import models
from django.utils.text import slugify

# Create your models here.

class Machine(models.Model):

    COFFEE_MACHINE_LARGE = 'CM10'
    COFFEE_MACHINE_SMALL = 'CM00'
    ESPRESSO_MACHINE = 'EM00'

    product_type_mach = (
        (COFFEE_MACHINE_LARGE,'COFFEE_MACHINE_LARGE'),
        (COFFEE_MACHINE_SMALL,'COFFEE_MACHINE_SMALL'),
        (ESPRESSO_MACHINE,'ESPRESSO_MACHINE')
    )

    model_type = (
        ('1','base_model'),
        ('2','premium_model'),
        ('3','deluxe_model'),
    )
    product_type_machine = models.CharField( max_length=50, choices= product_type_mach)
    model_types = models.CharField( max_length=50, choices= model_type)
    water_line_compatible = models.BooleanField()
    sku = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.sku = ''.join((slugify(self.product_type_machine), slugify(self.model_types)))
        super(Machine, self).save(*args, **kwargs)


    def __str__(self):
        return self.sku
    
