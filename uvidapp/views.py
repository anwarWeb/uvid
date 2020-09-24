from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Contact ,Jan_Aushadhi_Registration, DeliveryPartner,Appoitement,Department,Doctor
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage


# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/logout_users/')
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
        
        if "." not in email:
             return render(request,'contact_us.html',{'message':'Please Enter Valid Email.'})

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
     #    email = EmailMessage(name, message, to=['sourabhrathoresr2@gmail.com'])
     #    email.send()
    return render(request,'contact_us.html',{'message':'Message has been send !'})


def appointment(request):
     department=Department.objects.all()
     if request.method=="POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        Date = request.POST.get('Date',)
        gender = request.POST.get('gender', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        department = request.POST.get('department', '')
        doctors = request.POST.get('doctors', '')
        symptom = request.POST.get('subject', '')

        if "." not in email:
             return render(request,'appointment.html',{'msg':'Please Enter Valid Email.'})

        appoitement = Appoitement(first_name=first_name, last_name=last_name, Date=Date, gender=gender,email=email,phone_number=phone_number,department=department,doctor=doctors,symptom=symptom)
        appoitement.save()
        msg = "Your appoitment has been done"
        return render(request, 'appointment.html',{'msg':msg})
     return render(request, 'appointment.html',{'department':department})

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
        driving_licence = request.FILES['driving_licence']
        aadhar_card = request.FILES['aadhar_card']
        pan_card = request.FILES['pan_card']
        deliveryPartner = DeliveryPartner(name=name,phone=phone, email=email, message=message, driving_licence=driving_licence, aadhar_card=aadhar_card, pan_card=pan_card,)
        deliveryPartner.save()
     return render(request,'delivery_partner.html')

def signup(request):
     if request.method=="POST":
          username = request.POST['username']
          email = request.POST['email']
          fname = request.POST['fname']
          lname = request.POST['lname']
          password = request.POST['password']

          if User.objects.filter(email=email):
               messages.success(request,"Email id is allredy exits")

          else:
               myuser = User.objects.create_user(username,email,password,is_staff = True)
               myuser.first_name= fname
               myuser.last_name= lname
          
               myuser.save()
               messages.success(request,"Account has been successfull")
               return redirect('home')
    
     else:
          return HttpResponse("404 not found..")
     return render(request, 'home.html')


def login_users(request):
     if request.method=="POST":
          loginusername = request.POST['loginusername']
          loginpassword = request.POST['loginpassword']

     user = authenticate(username=loginusername, password=loginpassword)
     if user is not None:
          login (request, user)
          messages.success(request,"Login Successfully")
          return redirect('home')
     else:
          messages.error(request,"Failed")
          return redirect('home')

     return render(request, 'home.html')

def logout_users(request):
     logout(request)
     return redirect('home')


def load_courses(request):
    department_id = request.GET.get('department')
    print(department_id)
    doctors = Doctor.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'doctors':doctors})