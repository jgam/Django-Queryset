from django.db import models

# Create your models here.


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default='S')
    class Meta:
        db_table = 'Person db'

class Shirt(models.Model):#shirt is owned by one person but person has multiple shirts
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    brands = models.CharField(max_length=20, default='Nike')
    price = models.IntegerField()
    #you can also do recursive relationships with models.ForeignKey(...)




