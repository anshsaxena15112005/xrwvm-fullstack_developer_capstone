from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Optional extra field: establishment_year
    establishment_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    # Many-To-One relationship to Car Make
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    
    # Dealer ID (Refers to a dealer in Cloudant)
    dealer_id = models.IntegerField()
    
    name = models.CharField(max_length=100)
    
    # Type choices
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    HYBRID = 'Hybrid'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (HYBRID, 'Hybrid')
    ]
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default=SUV
    )
    
    # Year field with specific range validation
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"