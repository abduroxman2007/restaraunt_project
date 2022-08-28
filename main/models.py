from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='branch_img')
    location = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)


class Client(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, blank=True)
    first_name = models.CharField('first_name', max_length=200, null=True)
    last_name = models.CharField('last_name', max_length=200, null=True)
    image = models.ImageField(upload_to='users_img')
    phone_number = models.IntegerField('phone_number', null=True)

    def __str__(self) -> str:
        return self.first_name


class Food(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='foods_img')
    description = models.TextField(null=True)
    price = models.IntegerField('price', null=True)
    rate = models.FloatField(null=True)

    def __str__(self) -> str:
        return self.name


class Rating(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, related_name='client')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, related_name='food')
    rating = models.PositiveIntegerField(null=True, blank=False)

    # class Meta:
    #     unique_together = ('client', 'food') 


class Table(models.Model):
    people_size = models.IntegerField(null=True)
    image = models.ImageField(upload_to='table_img')
    number = models.IntegerField(null=True)
    part = models.IntegerField(null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


class TableOrder(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(null=False, default=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class OrderFood(models.Model):
    table_order = models.ForeignKey(TableOrder, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.FloatField()
