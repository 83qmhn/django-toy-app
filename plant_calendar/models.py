from django.conf import settings
from django.db import models


def get_fertilisers():
    return {i: i for i in settings.FERTILISERS}

def get_sunlight_conditions():
    return {i: i for i in settings.SUNLIGHT_CONDITIONS}


FERTILISERS = [
    ("TUISF", "Tui Seaweed & Fish Fertiliser"),
    ("TUICS", "Tui Chicken & Sheep"),
    ("YATESAP", "Yates Thrive All Purpose Liquid Plant Food"),
    ("YATESCF", "Yates Thrive Citrus and Fruit Fertiliser Granules"),
]

SUNLIGHT_CONDITIONS= [
    ("FS", "Full Sun"),
    ("PS", "Partially Shaded"),
    ("NS", "No SUN"),
]


class Plant(models.Model):
    name = models.CharField(max_length=100)
    # define suitably-named constant for each value
    SPRING = "S1"
    SUMMER = "S2"
    AUTUMN = "S3"
    WINTER = "S4"
    SEASONS_CHOICES = {
        SPRING: "Spring",
        SUMMER : "Summer",
        AUTUMN :"Autumn",
        WINTER : "Winter",
    }
    best_season_to_plant = models.CharField(max_length=2, choices=SEASONS_CHOICES, default=SPRING)

    def add(self):
        self.save()

    def __str__(self):
        return self.name

# models.Model means that the Class is a Django Model, so Django knows that it should be saved in the database.
class PlantCalendar(models.Model):
    plant_name = models.ForeignKey(Plant, on_delete=models.CASCADE)
    plant_date = models.DateField()
    harvest_date = models.DateField(blank=True, null=True) # blank is related to form validation

    TUI_LIQUID = "TUISF"
    TUI_SOLID = "TUICS"
    YATES_LIQUID = "YATESAP"
    YATES_SOLID = "YATESCF"

    FERTILISERS = {
    "TUISF": "Tui Seaweed & Fish Fertiliser",
    "TUICS": "Tui Chicken & Sheep",
    "YATESAP": "Yates Thrive All Purpose Liquid Plant Food",
    "YATESCF": "Yates Thrive Citrus and Fruit Fertiliser Granules"
    }

    fertiliser = models.CharField(max_length=20, choices=FERTILISERS)

    FS = "FS"
    PS = "PS"
    NS = "NS"
    SUNLIGHT_CHOICES = {
        "FS":  "Full Sun",
        "PS": "Partially Shaded",
        "NS": "No Sun",
    }
    plant_spot_sunlight_condition = models.CharField(max_length=2, choices=SUNLIGHT_CHOICES)

    def add(self):
        self.save()

    # TODO: search for showing the name of plant
    def __str__(self):
        return self.fertiliser