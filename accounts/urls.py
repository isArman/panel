from django.urls import path
from .views import register, login_view, home, add_contact, logout_view, view_contacts, send_sms


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('add_contact/', add_contact, name='add_contact'),
    path('logout/', logout_view, name='logout'),
    path('view_contacts/', view_contacts, name='view_contacts'),
    path('send_sms/', send_sms, name='send_sms'),  # اشاره به ویو جدید
]