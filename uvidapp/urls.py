from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('contactSave/', views.contactSave, name="contactSave"),
    path('appointment/', views.appointment, name="appointment"),
    path('order-tracking/', views.orderTracking, name="order-tracking"),
    path('priscription/', views.priscription, name="priscription"),
    path('test-booking/', views.testBooking, name="test-booking"),
    path('generic/', views.generic, name="generic"),
    path('ayurvedic/', views.ayurvedic, name="ayurvedic"),
    path('jan-aushadhi-kendra/', views.janAsuhadhiKendra, name="jan-aushadhi-kendra"),
    path('jan_aushadhi_kendra_Save/',views.jan_aushadhi_kendra_Save, name="jan_aushadhi_kendra_Save"),
    path('delivery-partner/', views.deliveryPartner, name="delivery-partner"),
    path('delivery_partner_Save/', views.deliveryPartnerSave, name="delivery_partner_Save"),
    path('signup/', views.signup, name="signup"),
    path('login_users/', views.login_users, name="login_users"),
    path('logout_users/', views.logout_users, name="logout_users"),

    path('load-courses/', views.load_courses, name='ajax_load_courses'),


    
]