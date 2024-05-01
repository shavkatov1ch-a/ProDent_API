from rest_framework import serializers
from .models import Contact, ContactInfo

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only = ['created', 'update']


class ContactInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'
        read_only = ['created', 'update']
