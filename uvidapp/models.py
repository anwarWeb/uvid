from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Doctor(models.Model):
    name= models.CharField(max_length=50,default="")
    doctor_type= models.CharField(max_length=50,choices=[('Generic', 'Generic'), ('Ayurvedic', 'Ayurvedic')])
    description=models.TextField(default="")
    stutas=models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="images/",default="")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name            

class Jan_Aushadhi_Registration (models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=70, default="")
    email = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=500, default="")
    land_agreement = models.ImageField(upload_to="images/",default="")
    aadhar_card = models.ImageField(upload_to="images/",default="")
    status_of_applicant = models.ImageField(upload_to="images/",default="")
    pharmacist_certificate = models.ImageField(upload_to="images/",default="")
    application_form = models.ImageField(upload_to="images/",default="")
    pan_card = models.ImageField(upload_to="images/",default="")
    society_registration_certificate = models.ImageField(upload_to="images/",default="")
    
    def __str__(self):
        return self.name  