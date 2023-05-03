from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    
class ShoppingSession(models.Model):
    shop_name = models.CharField(max_length=100)
    persons = models.ManyToManyField(Person)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_settled = models.BooleanField(default=False)

class PersonalShoppingSession(models.Model):
    shopping_session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    personal_price = models.DecimalField(max_digits=10, decimal_places=2)
    