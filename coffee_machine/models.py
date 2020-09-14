from django.db import models

# Create your models here.

product_type_mach = (
    ('COFFEE_MACHINE_LARGE','COFFEE_MACHINE_LARGE'),
    ('COFFEE_MACHINE_SMALL','COFFEE_MACHINE_SMALL'),
    ('ESPRESSO_MACHINE','ESPRESSO_MACHINE')
)

model_type = (
    ('base_model','base_model'),
    ('premium_model','premium_model'),
    ('deluxe_model','deluxe_model'),
)
class Machine(models.Model):
    product_type_machine = models.CharField( max_length=50, choices= product_type_mach)
    model_types = models.CharField( max_length=50, choices= model_type)
    water_line_compatible = models.BooleanField()
