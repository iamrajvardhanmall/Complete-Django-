from django.db import models

# Create your models here.

# Django Model Data Types and Fields List
class Musician(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    instrument = models.CharField(max_length= 200)
    
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    
    
    
# Field Validations and Built-In Fields - Django Models
class RajModel(models.Model):
    raj_field = models.IntegerField()
    def __str__(self):
        return str(self.raj_field)
    
    

# Custom Field Validations in Django Models

# from django.db.models import Model
# class customField(Model):
#     mail = models.CharField(max_length=200)
from django.core.exceptions import ValidationError
def validate_mail(value):
    if not value.endswith("@gmail.com"):
        raise ValidationError("This Field accepts only Gmail addresses.")

class customField(models.Model):
    mail = models.CharField(max_length=200, validators=[validate_mail])
    
    
    

# Relational fields in Django models
# Django supports three main types of relationships:
# Many-to-One (ForeignKey)
# Many-to-Many (ManyToManyField)
# One-to-One (OneToOneField)

# 1.) Many-to-one(ForeignKey)
class Album1(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
class Song1(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # Song belongs to one Album.
    # An Album can have many Song records.
    # ForeignKey defines the many-to-one relationship.
    # on_delete=models.CASCADE deletes songs if the album is deleted.

# 2.) Many-to-Many Fields
class Author(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    authors = models.ManyToManyField(Author)
    # A Book can have multiple Authors.
    # An Author can write multiple Books.
    # ManyToManyField defines the many-to-many relationship.
    
# 3.) One-to-One Fields
class Vehicle(models.Model):
    reg_no = models.IntegerField()
    owner = models.CharField(max_length=100)
class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    car_model = models.CharField(max_length=100)
    # Each Car is linked to exactly one Vehicle.
    # Each Vehicle can have at most one Car.
    # OneToOneField defines the one-to-one relationship.
    # on_delete=models.CASCADE deletes the Car if the linked Vehicle is deleted.

    
    

# Django ORM - Inserting, Updating & Deleting Data
# Django’s ORM (Object Relational Mapper) makes database work easier by letting developers use Python classes instead of writing SQL.
class Album2(models.Model):
    title = models.CharField(max_length = 30)
    artist = models.CharField(max_length = 30)
    genre = models.CharField(max_length = 30)
    def __str__(self):   # The __str__() method returns a readable string representation of the object.
        return self.title

class Song2(models.Model):
    name = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)

    def __str__(self):
        return self.name