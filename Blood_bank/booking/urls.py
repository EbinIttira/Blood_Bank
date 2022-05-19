from django.urls import path
from .import views
app_name='booking'
urlpatterns=[
    path('',views.home,name='home'),
    path('donor_register/',views.donor_register,name="donor_register")
]