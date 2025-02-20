from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    img = models.ImageField(upload_to='persons/')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Contact(models.Model):
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    email1 = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    email3 = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social1 = models.CharField(blank=True, null=True, max_length=30)
    social2 = models.CharField(blank=True, null=True, max_length=30)
    social3 = models.CharField(blank=True, null=True, max_length=30)
    
    def __str__(self):
        return 'Contact Information'