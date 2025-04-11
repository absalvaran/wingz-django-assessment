from django.db import models

class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)