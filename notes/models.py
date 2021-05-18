from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=13, null=True)
    role = models.CharField(max_length=20, null=True)
    branch = models.CharField(max_length=40, null=True)

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=13, null=True)
    subject = models.CharField(max_length=20)
    branch = models.CharField(max_length=40, null=True)
    filetype = models.CharField(max_length=40, null=True)
    notesfile = models.FileField(null=True)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=40)

class Feedback(models.Model):
    uploadingdate = models.CharField(max_length=13, null=True)
    name = models.CharField(max_length=40)
    contact = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=40, null=True)
    description = models.CharField(max_length=2000, null=True)

class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=13, null=True)
    file = models.FileField(null=True)
    description = models.CharField(max_length=200, null=True)
    fav = models.CharField(max_length=200, null=True, default='no')

class Notepad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=13, null=True)
    content = models.CharField(max_length=900, null=True)
    filename = models.CharField(max_length=200, null=True)
