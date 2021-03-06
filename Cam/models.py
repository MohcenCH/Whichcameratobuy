from django.db import models

class Product(models.Model):

    Name = models.CharField(max_length=700, null=True)
    BRAND = (
			('Nikon', 'Nikon'),
			('Canon', 'Canon'),
			('Sony', 'Sony'),
            ('Pentax', 'Pentax'),
			('Olympus', 'Olympus'),
			('Lumix', 'Lumix'),
			('Fujifilm', 'Fujifilm'),
			('Leica', 'Leica'),
			('', ''),
			('', ''),

			)
    Price = models.FloatField(null=True)
    Link = models.URLField(max_length=2000, null=True)
    Image_Link = models.URLField(max_length=2000, null=True)
    #Image = models.ImageField(upload_to = 'product-img/', null=True)
    Continuous_shooting = models.FloatField(null=True)
    Focus_type = models.CharField(max_length=700, null=True)
    Max_resolution = models.FloatField(null=True)
    Style = models.CharField(max_length=700, null=True)
    Video_resolution = models.CharField(max_length=700, null=True)
    Wireless_communication_technology = models.CharField(max_length=700, null=True)
    description = models.CharField(max_length=4000, null=True)

    def __str__(self):
        return self.Name



    











	