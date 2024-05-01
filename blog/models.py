from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='home')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title


class Post(models.Model):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='posts')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title






class Service(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class About(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='about')
    doctors = models.CharField(max_length=212)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='blog')
    author = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title






