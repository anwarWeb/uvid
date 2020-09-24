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


    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.thumbnail.url))
        return ""

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

    @property
    def land_agreement_preview(self):
        if self.land_agreement:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.land_agreement.url))
        return ""

    @property
    def aadhar_card_preview(self):
        if self.aadhar_card:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.aadhar_card.url))
        return ""


    @property
    def status_of_applicant_preview(self):
        if self.status_of_applicant:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.status_of_applicant.url))
        return ""

    @property
    def pharmacist_certificate_preview(self):
        if self.pharmacist_certificate:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.pharmacist_certificate.url))
        return ""

    @property
    def application_form_preview(self):
        if self.application_form:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.application_form.url))
        return ""


    @property
    def pan_card_preview(self):
        if self.pan_card:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.pan_card.url))
        return ""


    @property
    def society_registration_certificate_preview(self):
        if self.society_registration_certificate:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.society_registration_certificate.url))
        return ""

        
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

    @property
    def driving_licence_preview(self):
        if self.driving_licence:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.driving_licence.url))
        return ""

    @property
    def aadhar_card_preview(self):
        if self.aadhar_card:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.aadhar_card.url))
        return ""


    @property
    def pan_card_preview(self):
        if self.pan_card:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.pan_card.url))
        return ""


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

