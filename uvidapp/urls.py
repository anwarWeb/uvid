from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('appointment/', views.appointment, name="appointment"),
    path('order-tracking/', views.orderTracking, name="order-tracking"),
    path('priscription/', views.priscription, name="priscription"),
    path('test-booking/', views.testBooking, name="test-booking"),
    path('generic/', views.generic, name="generic"),
    
    path('ayurvedic/', views.ayurvedic, name="ayurvedic"),
    path('jan-aushadhi-kendra/', views.janAsuhadhiKendra, name="jan-aushadhi-kendra"),
    path('delivery-partner/', views.deliveryPartner, name="delivery-partner"),
]