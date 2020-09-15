from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def contact_us(request):
    return render(request, 'contact_us.html')

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

def deliveryPartner(request):
     return render(request, 'delivery_partner.html') 