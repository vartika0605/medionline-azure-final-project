from datetime import date
from django.utils.translation import ugettext_lazy as _
from django import forms
import datetime

#from datetimewidget.widgets import DateTimeWidget

from .models import Appointment
from .models import Doctor,Prescription
class MyDateInput(forms.DateInput):
    input_type = "date"





class DoctorForm(forms.ModelForm):
    CATEGORIES = (
         ('09:00-10:00','09:00-10:00'),
        ('10:00-11:00','10:00-11:00'),
        ('11:00-12:00','11:00-12:00'),
        ('12:00-01:00','12:00-01:00'),
    )

    timeslots = forms.MultipleChoiceField(choices=CATEGORIES, widget=forms.CheckboxSelectMultiple,)
    class Meta:
        model=Doctor
        fields = ['name','speciality','doc_price','meeting_link','timeslots','profile_pic','experience','address_of_your_workplace']
        labels = {
            'doc_price': _('Price'),
        }
        



    
            
    

class uploadForm(forms.ModelForm):
     
    
    class Meta:
        model = Prescription
        fields = (
            "file_field",
            "patientUsername",
            "description",

        )
