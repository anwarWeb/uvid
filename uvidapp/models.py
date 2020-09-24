from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name

class Doctor(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
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

        
class DeliveryPartner(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=70, default="")
    email = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")
    driving_licence = models.ImageField(upload_to="images/",default="")
    aadhar_card = models.ImageField(upload_to="images/",default="")
    pan_card = models.ImageField(upload_to="images/",default="")
    
    def __str__(self):
        return self.name


class Appoitement(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70, default="")
    Date = models.DateField(blank=True, default='', null=True)
    gender = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=50, default="")
    phone_number = models.CharField(max_length = 11 ,default="")
    department = models.CharField(max_length=50, default="")
    doctor = models.CharField(max_length=50, default="")
    symptom = models.ImageField(upload_to="images/",default="")
    
    def __str__(self):
        return self.name

class Member(models.Model):
       residing_country = models.CharField(max_length=50)
       residing_state = models.CharField(max_length=50)
       residing_city = models.CharField(max_length=50)

       def __str__(self):
           return self.residing_country

