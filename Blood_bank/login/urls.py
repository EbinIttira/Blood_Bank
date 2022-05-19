from . import views
from django . urls import path
app_name='login'
urlpatterns=[
    path('',views.login,name="login"),
    path('user_login/',views.user_page,name="user_page"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
]