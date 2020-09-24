from django.contrib import admin
from django.db import models
from .models import Doctor, Contact, Jan_Aushadhi_Registration, DeliveryPartner, Appoitement, Member, Country, State, City, Department


# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
     list_display = ('name',)

admin.site.register(Department, DepartmentAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','doctor_type','description','stutas','thumbnail')
    readonly_fields = ('thumbnail_preview',)


    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
    
admin.site.register(Doctor, DoctorAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email','message')

admin.site.register(Contact, ContactAdmin)


class Jan_Aushadhi_RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email','address','land_agreement','aadhar_card','status_of_applicant','pharmacist_certificate','application_form','pan_card','society_registration_certificate',)
    readonly_fields = ('land_agreement_preview', 'aadhar_card_preview', 'status_of_applicant_preview', 'pharmacist_certificate_preview', 'application_form_preview', 'pan_card_preview', 'society_registration_certificate_preview')


    def land_agreement_preview(self, obj):
        return obj.land_agreement_preview

    land_agreement_preview.short_description = 'Land Agreement Preview'
    land_agreement_preview.allow_tags = True


    def aadhar_card_preview(self, obj):
        return obj.aadhar_card_preview

    aadhar_card_preview.short_description = 'Aadhar Card Preview'
    aadhar_card_preview.allow_tags = True


    def status_of_applicant_preview(self, obj):
        return obj.status_of_applicant_preview

    status_of_applicant_preview.short_description = 'Status of Applicant Preview'
    status_of_applicant_preview.allow_tags = True


    def pharmacist_certificate_preview(self, obj):
        return obj.pharmacist_certificate_preview

    pharmacist_certificate_preview.short_description = 'Pharmacist Certificate Preview'
    pharmacist_certificate_preview.allow_tags = True


    def application_form_preview(self, obj):
        return obj.application_form_preview

    application_form_preview.short_description = 'Application Form Preview'
    application_form_preview.allow_tags = True


    def pan_card_preview(self, obj):
        return obj.pan_card_preview

    pan_card_preview.short_description = 'Pan Card Preview'
    pan_card_preview.allow_tags = True



    def society_registration_certificate_preview(self, obj):
        return obj.society_registration_certificate_preview

    society_registration_certificate_preview.short_description = 'Society Registration Certificate Preview'
    society_registration_certificate_preview.allow_tags = True

admin.site.register(Jan_Aushadhi_Registration,Jan_Aushadhi_RegistrationAdmin)


class DeliveryPartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'message', 'driving_licence', 'aadhar_card', 'pan_card',)
    readonly_fields = ('driving_licence_preview', 'aadhar_card_preview', 'pan_card_preview',)

    def driving_licence_preview(self, obj):
        return obj.driving_licence_preview

    driving_licence_preview.short_description = 'Driving Licence Preview'
    driving_licence_preview.allow_tags = True


    def aadhar_card_preview(self, obj):
        return obj.aadhar_card_preview

    aadhar_card_preview.short_description = 'Aadhar Card Preview'
    aadhar_card_preview.allow_tags = True


    def pan_card_preview(self, obj):
        return obj.pan_card_preview

    pan_card_preview.short_description = 'Pan Card Preview'
    pan_card_preview.allow_tags = True
    
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
