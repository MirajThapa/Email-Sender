from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.email_sender, name ="email_sender"),
    path('email/sent/success/', views.email_sent_success, name='email_sent_success'),
]