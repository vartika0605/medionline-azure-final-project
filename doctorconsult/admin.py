from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.


admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Property)
