from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class hospitalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    
class plasmabankUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)


class Donor(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    blood = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    # address = models.CharField(max_length=50)
    query1 = models.CharField(max_length=10)
    query2 = models.CharField(max_length=10)
    query3 = models.CharField(max_length=10)
    query4 = models.CharField(max_length=10)
    query5 = models.CharField(max_length=10)
    query6 = models.CharField(max_length=10)
    query7 = models.CharField(max_length=10)


    def __str__(self):
        return self.fname

class donor_feedback(models.Model):
    ftitle = models.CharField(max_length = 50)
    plasma_bank = models.CharField(max_length=20)
    review = models.CharField(max_length = 50)
    feedback = models.CharField(max_length = 100)
    # donor_id = models.IntegerField()
    submission_date = models.DateField()

    def __str__(self):
        return self.plasma_bank

class hospital_feedback(models.Model):
    ftitle = models.CharField(max_length=50)
    review = models.CharField(max_length=50)
    feedback = models.CharField(max_length=100)
    hospital = models.CharField(max_length=50)
    plasma_bank = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateField()
    

class blooddetail(models.Model):
    donor = models.OneToOneField(Donor, on_delete=models.CASCADE, unique=True)
    blood_group = models.CharField(max_length=10)
    rhtype = models.CharField(max_length=20)
    plate = models.CharField(max_length=20)
    wbc = models.CharField(max_length=20)
    antibody = models.CharField(max_length=20)

class dnumber(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    number = models.IntegerField()
    def __str__(self):
        return self.user

class donation_plasma_bank(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    number = models.IntegerField()
    def __str__(self):
        return self.user

class available(models.Model):
    donor = models.OneToOneField(Donor, on_delete=models.CASCADE)
    available = models.BooleanField()