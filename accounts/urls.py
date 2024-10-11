from django.urls import path
from .views import register, login_view, home, add_contact, logout_view, view_contacts


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('add_contact/', add_contact, name='add_contact'),
    path('logout/', logout_view, name='logout'),
    path('view_contacts/', view_contacts, name='view_contacts'),
]