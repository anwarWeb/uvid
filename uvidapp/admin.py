from django.contrib import admin
from django.db import models
from .models import Doctor,Contact,Jan_Aushadhi_Registration,DeliveryPartner,Appoitement,Member,Country,State,City


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


class DeliveryPartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email','message','driving_licence','aadhar_card','pan_card',)
admin.site.register(DeliveryPartner,DeliveryPartnerAdmin)

class AppoitementAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'Date','gender','email','phone_number','symptom',)
admin.site.register(Appoitement,AppoitementAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('residing_country', 'residing_country', 'residing_country',)
admin.site.register(Member,MemberAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('country',)
admin.site.register(Country,CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ('state', 'country',)
admin.site.register(State,StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'state',)
admin.site.register(City,CityAdmin)
