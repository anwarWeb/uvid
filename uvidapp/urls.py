from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    # path('contactSave',views.contactSave),
    # path('about-us/', views.about_us, name="about_us"),
    # path('services/', views.services, name="services"),
    # path('services_view/<int:myid>',views.servicesView),
    # path('order/',views.orederform),
    # path('orderSave',views.orderSave),
]