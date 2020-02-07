from django.db import models

# Create your models here.


class Topping(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )


class Restaurant(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=120)
    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(
        Pizza, related_name='championed_by', on_delete=models.CASCADE)
