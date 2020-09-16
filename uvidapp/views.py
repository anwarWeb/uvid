from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact ,Jan_Aushadhi_Registration

# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def contactSave(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request,'contact_us.html',{'message':'Message has been send !'})

def appointment(request):
    return render(request, 'appointment.html')

def orderTracking(request):
    return render(request, 'order_tracking.html')

def priscription(request):
     return render(request, 'priscription.html')

def testBooking(request):
     return render(request, 'test_booking.html')

def generic(request):
     return render(request, 'generic.html') 

def ayurvedic(request):
     return render(request, 'ayurvedic.html') 

def janAsuhadhiKendra(request):
     return render(request, 'jan_asuhadhi_kendra.html') 

def jan_aushadhi_kendra_Save(request):
     if request.method=="POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        land_agreement = request.FILES['land_agreement']
        aadhar_card =  request.FILES['aadhar_card']
        status_of_applicant =  request.FILES['status_of_applicant']
        pharmacist_certificate =  request.FILES['pharmacist_certificate']
        application_form =  request.FILES['application_form']
        pan_card =  request.FILES['pan_card']
        society_registration_certificate =  request.FILES['society_registration_certificate']
        Aushadhi_Registration = Jan_Aushadhi_Registration(name=name,phone=phone, email=email, address=address, land_agreement=land_agreement, aadhar_card=aadhar_card, status_of_applicant=status_of_applicant, pharmacist_certificate=pharmacist_certificate, application_form=application_form, pan_card=pan_card, society_registration_certificate=society_registration_certificate )
        Aushadhi_Registration.save()
     return render(request,'jan_asuhadhi_kendra.html')

def deliveryPartner(request):
     return render(request, 'delivery_partner.html')


def deliveryPartnerSave(request):
     if request.method=="POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        driving_icence =  request.FILES['driving_icence']
        aadhar_card =  request.FILES['aadhar_card']
        pan_card =  request.FILES['pan_card']
     return render(request,'delivery_partner.html')