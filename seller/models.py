from django.db import models
from django.forms import ValidationError

from master.models import baseModel
from master.utils.LO_UNIQUE.unique_filename import genrate_unique_filename
from master.utils.LO_CALC.calc import calculate_discount

# Create your models here.

class categoriesModel(baseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class productsModel(baseModel):
    DIR_NAME = 'product_images/'
    SUFFIX_WORD = 'pi'
    image = models.ImageField(upload_to=genrate_unique_filename)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category_id = models.ForeignKey(categoriesModel, on_delete=models.CASCADE)
    mrp_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    def clean(self):
        if self.mrp_price < self.selling_price:
            raise ValidationError("Selling price cannot be greater than MRP price")

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate before saving
        self.discount = calculate_discount(self.mrp_price, self.selling_price)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category_id.name} - {self.title}"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    