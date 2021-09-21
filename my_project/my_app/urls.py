from django.conf.urls import  url
from my_app import views

my_app = 'base_app'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name="user_login"),
    
]