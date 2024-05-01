from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=212)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    address = models.TextField()
    time = models.CharField(max_length=212)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address


