from django.urls import path
from .views import Company, Contact, Map
from django.views.generic import RedirectView


urlpatterns = [
    path('', Company.as_view(), name='company'),
    path('contact/', Contact.as_view(), name='contact'),
    path('contact/<str:slug>', RedirectView.as_view(url='/company/contact/')),
    path('map/', Map.as_view(), name='map'),
]