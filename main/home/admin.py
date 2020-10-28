from django.contrib import admin
from .models import Donor, dnumber, blooddetail, hospitalUser,plasmabankUser, donor_feedback, hospital_feedback, available, donation_plasma_bank

# Register your models here.
admin.site.register(Donor)
# admin.site.register(Dnumber)
admin.site.register(dnumber)
admin.site.register(donation_plasma_bank)
admin.site.register(blooddetail)
admin.site.register(hospitalUser)
admin.site.register(plasmabankUser)
admin.site.register(donor_feedback)
admin.site.register(hospital_feedback)
admin.site.register(available)
