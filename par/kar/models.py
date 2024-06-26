from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES=(
    ('sm','Sumsung'),
    ('ap','apple'),
    ('xi','xiaomi')
)

STATE_CHOICES=(
    ('pb','Port Blair '),
    ('am','america'),
    ('D','Delhi')
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length =2)
    product_image =models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    


class Customer(models.Model):
    user=models.ForeignKey( User ,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def _str_(self):
        return self.name 
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)


   # @property
    #def total_cost(self):
     #   return self.quantity * self.product.discounted_price
