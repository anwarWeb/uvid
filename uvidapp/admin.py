from django.contrib import admin
from django.db import models
from .models import Doctor,Contact,Jan_Aushadhi_Registration  

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','doctor_type','description','stutas','thumbnail')
admin.site.register(Doctor, DoctorAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email','message')

admin.site.register(Contact, ContactAdmin)


class Jan_Aushadhi_RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email','address','land_agreement','aadhar_card','status_of_applicant','pharmacist_certificate','application_form','pan_card','society_registration_certificate',)
admin.site.register(Jan_Aushadhi_Registration,Jan_Aushadhi_RegistrationAdmin)