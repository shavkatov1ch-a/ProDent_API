from django.urls import path
from .views import ContactInfoAPIView, ContactAPIView

urlpatterns = [
    path('', ContactAPIView.as_view(), name='contact'),
    path('info/', ContactInfoAPIView.as_view(), name='contact-info'),

]