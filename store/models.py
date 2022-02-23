from django.core.validators import MinValueValidator
from random import choices
from django.db import models

#collections model
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    
    def __str__(self) -> str:
        return self.title



# products model
class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(0)])
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.title
    
    #order by title
    class meta:
        ordering = ['title',]
    
    
#customer model
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
        ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField (max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices = MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    
    def __str__(self) -> str:
        return self.title



class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class Order(models.Model):
    PENDING = 'P'
    COMPLETE = 'C'
    FAILED = 'F'
    
    STATUS = [ 
        (PENDING, 'Pending'),
        (COMPLETE, 'Completed'),
        (FAILED, 'Failed'),
        ]
    payment_status = models.CharField(max_length=1, choices=STATUS, default=PENDING)
    placed_at =models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.title
    
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField ()
    unit_price = models.DecimalField (max_digits=6, decimal_places=2)
    
    def __str__(self) -> str:
        return self.title
    
    
    
class Cart (models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    
    def __str__(self) -> str:
        return self.title
    
    