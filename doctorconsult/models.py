

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from multiselectfield import MultiSelectField
from django.utils.translation import ugettext_lazy as _
#from datetimewidget.widgets import DateTimeWidget
# Create your models here.




class Property(models.Model):
    """ Docstring """
    name = models.CharField(max_length=128)
    def __str__(self):
        return f'{self.name}'

    

class Doctor(models.Model):
   
    username=models.CharField(max_length=100,primary_key=True)
    department = (
        ('Dentistry', "Dentistry"),
        ('Cardiology', "Cardiology"),
        ('ENT Specialists', "ENT Specialists"),
        ('Astrology', 'Astrology'),
        ('Neuroanatomy', 'Neuroanatomy'),
        ('Blood Screening', 'Blood Screening'),
        ('Eye Care', 'Eye Care'),
        ('Physical Therapy', 'Physical Therapy'),
    )

   
    doc_price= models.FloatField()
    name=models.CharField(max_length=100)
    speciality=models.CharField(choices=department,max_length=100)
    meeting_link = models.URLField(max_length=2000)
    timeslots = models.ManyToManyField(Property)
    address_of_your_workplace= models.CharField(max_length=100,null=True, blank=True)
    experience=models.IntegerField(null=True, blank=True)
    profile_pic = models.FileField(upload_to='doctors/',null=True, blank=True,)
    
    def __str__(self):
        return f'{self.username} ({self.speciality})'

   
    






    





class Appointment(models.Model):

    

    TIMESLOT_LIST=(
        ('09:00-10:00','09:00-10:00'),
        ('10:00-11:00','10:00-11:00'),
        ('11:00-12:00','11:00-12:00'),
        ('12:00-01:00','12:00-01:00'),
    )
    datetime_start = models.DateTimeField(default=datetime.now)
    datetime_end = models.DateTimeField(default=datetime.now)


    #from models import Doctor.username
    #patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=100,default="")
    patient_age=models.IntegerField(default=1)
    doctor_name=models.CharField(max_length=100,default="")
    
    #doctorname=doctor.name(default="Ram")
    timeslot=models.CharField(choices=TIMESLOT_LIST,max_length=100)
    date = models.DateField(blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    ready_for_payment= models.BooleanField(default = False)
    


class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    file_field = models.FileField(upload_to='patients/')
    patientUsername = models.CharField(max_length=200)
    

    def __str__(self):
        return f'{self.doctor}=> {self.patientUsername}'



class Patient(models.Model):
    username=models.CharField(max_length=100,primary_key=True)
    id = models.AutoField
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=1)
    prescription = models.ManyToManyField(Prescription)
    def __str__(self):
        return f'{self.username}'
    

class Cart(models.Model):
    username=models.CharField(max_length=100,primary_key=True)
    
    docname=models.CharField(max_length=100)
    price=models.FloatField()
    order_id =  models.CharField(unique=True, max_length=100, null=True, blank=True, default=None) 
    datetime_start = models.DateTimeField(default=datetime.now)
    datetime_end = models.DateTimeField(default=datetime.now)

   
    def __str__(self):
        return f'{self.username}'




class Order(models.Model):
    status_choices = (
        (1, 'Not Packed'),
        (2, 'Ready For Shipment'),
        (3, 'Shipped'),
        (4, 'Delivered')
    )
    payment_status_choices = (
        (1, 'SUCCESS'),
        (2, 'FAILURE' ),
        (3, 'PENDING'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices = status_choices, default=1)

    total_amount = models.FloatField()
    payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, default=None) 
    datetime_of_payment = models.DateTimeField(default=timezone.now)
    # related to razorpay
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)
    docname=models.CharField(max_length=100, null=True, blank=True)
    datetime_start = models.DateTimeField(default=datetime.now)
    datetime_end = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.datetime_of_payment and self.id:
            self.order_id = self.datetime_of_payment.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.email + " " + str(self.id)
    



