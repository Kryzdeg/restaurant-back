from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", default="default.png")
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.CharField(max_length=255)
    meal_type = models.CharField(max_length=10, default='dinner')

    def __str__(self):
        return self.name