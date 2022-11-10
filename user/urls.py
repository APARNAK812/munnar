from django.urls import path
from.import views 
app_name='user'



urlpatterns=[
    path('home',views.home,name='home1'),
    path('contact',views.contact,name='contact1'),
    path('thingstodo',views.thingstodo,name='thingstodo1'),
    path('membership',views.membership,name='membership1'),
    path('packages',views.packages,name='packages1'),
]