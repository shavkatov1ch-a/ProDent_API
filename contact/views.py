from django.shortcuts import render
from rest_framework import generics
from .models import Contact, ContactInfo
from .serializers import ContactSerializer, ContactInfoSerializers



class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoAPIView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializers