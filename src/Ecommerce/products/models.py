from django.db import models
from Users.models import CustomUser
from catergory.models import Category
from store.models import Store
# Create your models here.


class Products(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    Name = models.CharField(max_length=100)
    Description = models.TextField(blank=True, null=True)
    Category = models.ForeignKey(Category, related_name='products_catergory', on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2), 
    Currency = models.CharField(max_length=3, default='USD'), # Default currency is USD
    quantity = models.PositiveIntegerField(null=False, default=0)
    imageUrl = models.URLField()
    Created_by = models.ForeignKey(CustomUser, related_name='product_owner', on_delete=models.CASCADE)
    Updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)  # Track how many times the product is viewed
    store_id = models.ForeignKey(Store, related_name="store", on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return '{} {}'.format(self.Price, self.Name)




