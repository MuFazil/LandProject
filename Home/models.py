from django.db import models

class Property(models.Model):
    # PROPERTY_CHOICES = [
    #     ('Apartment', 'Apartment'),
    #     ('Villa', 'Villa'),
    #     ('Independent House', 'Independent House'),
    #     ('Commercial Space', 'Commercial Space'),
    #     ('Land', 'Land'),
    # ]
    property_name = models.CharField(max_length=100)
    builder_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    images = models.ImageField(upload_to='property_images/')
    city_name = models.CharField(max_length=100)
    area_range_sqft = models.IntegerField(default=0)
    bhk_range = models.IntegerField(default=1)
    floor_plan = models.ImageField(upload_to='floor_plans/')
    amenities = models.JSONField(default=dict)  # Providing an empty dictionary as the default value
    brief_about_property = models.TextField(default = 'NA')
    about_builder = models.TextField(default = 'NA')

    def __str__(self):
        return self.property_name
