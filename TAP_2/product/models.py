from django.db import models

class Category(models.Model):
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category_name

    category_name = models.CharField(max_length=100)

class Drink(models.Model):
    class Meta:
        db_table = "drink"

    def __str__(self):
        return self.drink_name

    drink_name = models.CharField(max_length=100)
    drink_category = models.ManyToManyField(Category)
    information = models.CharField(max_length=100)
    allergy = models.CharField(max_length=100)

