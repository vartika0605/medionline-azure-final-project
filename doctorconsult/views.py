

# Create your views here.

from django.views import generic
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import render, redirect,HttpResponse

from .forms import DoctorForm,uploadForm
from .models import Appointment,Doctor,Patient,Prescription,Order,Cart,Property
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
import razorpay
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from io import BytesIO
import datetime
import time
from django.contrib.auth.models import User
import smtplib,ssl
from django.template.loader import get_template
from xhtml2pdf import pisa
import os


razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

 
 
def link(request):
    a= User.objects.get(username = request.user)
    order_list = list(Order.objects.all().filter(user = a))
    
    current_meeting = None

    for order_db in order_list:
        docname = order_db.docname
        username= order_db.user.username
        doctor= Doctor.objects.get(username=docname)
        meeting = doctor.meeting_link
        start_time =order_db.datetime_start
        end_time =  order_db.datetime_end
       # print(start_time)
       # print(end_time)
       #print(start_time.timestamp())
       #print(end_time.timestamp())
       # print(datetime.datetime.now().timestamp())
        now = datetime.datetime.now() # current date and time


        year = int(start_time.strftime("%Y"))
        print("year:", year)
        
        month = int(start_time.strftime("%m"))
        print("month:", month)
        
        day = int(start_time.strftime("%d"))
        print("day:", day)

        h = int(start_time.strftime("%H"))
        print("HOUR", h)
        
        min = int(start_time.strftime("%M"))
        print("MIN:", min)
        
        sec = int(start_time.strftime("%S"))
        print("sec", sec)
        
        
        start_time = datetime.datetime(year,month,day, h ,min,sec)



        year = int(end_time.strftime("%Y"))
        print("year:", year)
        
        month = int(end_time.strftime("%m"))
        print("month:", month)
        
        day = int(end_time.strftime("%d"))
        print("day:", day)

        h = int(end_time.strftime("%H"))
        print("HOUR", h)
        
        min = int(end_time.strftime("%M"))
        print("MIN:", min)
        
        sec = int(end_time.strftime("%S"))
        print("sec", sec)
        
        
        end_time = datetime.datetime(year,month,day, h ,min,sec)




        year = int(now.strftime("%Y"))
        print("year:", year)
        
        month = int(now.strftime("%m"))
        print("month:", month)
        
        day = int(now.strftime("%d"))
        print("day:", day)

        h = int(now.strftime("%H"))
        print("HOUR", h)
        
        min = int(now.strftime("%M"))
        print("MIN:", min)
        
        sec = int(now.strftime("%S"))
        print("sec", sec)
        
        
        datecur = datetime.datetime(year,month,day, h ,min,sec)
        print(datecur)
        
        print(datecur.timestamp())
        print(start_time.timestamp())
        print(end_time.timestamp())

        if ((datecur.timestamp()< start_time.timestamp()) or (datecur.timestamp()>end_time.timestamp())):
            continue
            
        current_meeting = meeting
        print(current_meeting)
    if current_meeting == None:
        return render(request, 'nomeetings.html')
    else:
        return render(request, 'linktoclick.html', {'obj': current_meeting})

   
        




   













@login_required
def appointment(request,user_name):
    doctor5 = get_object_or_404(Doctor, username=user_name)
    

    if request.method=='POST':
        
        
        
            patientname=   request.POST.get('name')
            patientage=   request.POST.get('age')

            if not Patient.objects.filter(username=request.user.username).exists():
                PatientProfile= Patient.objects.create(username = request.user.username,name =patientname,age=patientage)
                PatientProfile.save()
            
            irr =  request.POST.get('options')
            print("edfregdvredgggw",irr)
            
       
            if irr=='11':
                date=datetime.datetime.today()
                timeslot='09:00-10:00'
            if irr=='12':
                date=datetime.datetime.today()
                timeslot='10:00-11:00'
            if irr=='13':
                date=datetime.datetime.today()
                timeslot='11:00-12:00'
            if irr=='14':
                date=datetime.datetime.today()
                timeslot='12:00-13:00'
            if irr=='21':
                date=  datetime.datetime.today() + datetime.timedelta(days=1)
                timeslot='09:00-10:00'
            if irr=='22':
                date=  datetime.datetime.today() + datetime.timedelta(days=1)
                timeslot='10:00-11:00'
            if irr=='23':
                date=  datetime.datetime.today() + datetime.timedelta(days=1)
                timeslot='11:00-12:00'
            if irr=='24':
                date=  datetime.datetime.today() + datetime.timedelta(days=1)
                timeslot='12:00-13:00'    

            if irr=='31':
                date=  datetime.datetime.today() + datetime.timedelta(days=2)
                timeslot='09:00-10:00'
            if irr=='32':
                date=  datetime.datetime.today() + datetime.timedelta(days=2)
                timeslot='10:00-11:00'
            if irr=='33':
                date=  datetime.datetime.today() + datetime.timedelta(days=2)
                timeslot='11:00-12:00'
            if irr=='34':
                date=  datetime.datetime.today() + datetime.timedelta(days=2)
                timeslot='12:00-13:00'    

            if irr=='41':
                date=  datetime.datetime.today() + datetime.timedelta(days=3)
                timeslot='09:00-10:00'
            if irr=='42':
                date=  datetime.datetime.today() + datetime.timedelta(days=3)
                timeslot='10:00-11:00'
            if irr=='43':
                date=  datetime.datetime.today() + datetime.timedelta(days=3)
                timeslot='11:00-12:00'
            if irr=='44':
                date=  datetime.datetime.today() + datetime.timedelta(days=3)
                timeslot='12:00-13:00'    

            if irr=='51':
                date=  datetime.datetime.today() + datetime.timedelta(days=4)
                timeslot='09:00-10:00'
            if irr=='52':
                date=  datetime.datetime.today() + datetime.timedelta(days=4)
                timeslot='10:00-11:00'
            if irr=='53':
                date=  datetime.datetime.today() + datetime.timedelta(days=4)
                timeslot='11:00-12:00'
            if irr=='54':
                date=  datetime.datetime.today() + datetime.timedelta(days=4)
                timeslot='12:00-13:00'                
            

            post= Appointment(patient_name = patientname,patient_age=patientage,user=request.user,ready_for_payment = True,doctor_name = user_name,date=date,timeslot=timeslot)
            
            post.save()

            


            year = int(post.date.strftime("%Y"))
         #   print(year)
        #    print(type(year),"fgt")
            month =  int(post.date.strftime("%m"))
            day =  int(post.date.strftime("%d"))
            #print("jgvuuuuuuu",post.datetime_start)
           
            if post.timeslot == '09:00-10:00':
                post.datetime_start=datetime.datetime(year,month,day, 9 ,0,0)
                post.datetime_end=datetime.datetime(year,month,day, 10 ,0,0)
            if post.timeslot == '10:00-11:00':
                post.datetime_start=datetime.datetime(year,month,day, 10 ,0,0)
                post.datetime_end=datetime.datetime(year,month,day, 11 ,0,0)
            if post.timeslot == '11:00-12:00':
                post.datetime_start=datetime.datetime(year,month,day, 11 ,0,0)
                post.datetime_end=datetime.datetime(year,month,day, 12 ,0,0)
            if post.timeslot == '12:00-01:00':
                post.datetime_start=datetime.datetime(year,month,day, 12 ,0,0)
                post.datetime_end=datetime.datetime(year,month,day, 1 ,0,0)            
            post.save()
            
            datetime_start = post.datetime_start
            datetime_end = post.datetime_end
           # print("jgv",post.datetime_start)
            price_obj=Doctor.objects.get(username=user_name)
            price=price_obj.doc_price
            if Cart.objects.filter(username = request.user.username).first():
                Cart.objects.filter(username = request.user.username).update(username=request.user.username,docname=user_name,price=price,datetime_start=datetime_start,datetime_end=datetime_end)
            else:
                Cart.objects.create(username=request.user.username,docname=user_name,price=price,datetime_start=datetime_start,datetime_end=datetime_end )

            order_db = Order.objects.filter(docname=user_name).filter(datetime_start= datetime_start ).count()    
            if order_db== 5:
                return render(request, 'fail.html')
            
            return  redirect('/doctor/indexpay/')
        
       
        
        
    else:
        context={}
        
        obj1 = datetime.datetime.today()
        obj2 =  datetime.datetime.today() + datetime.timedelta(days=1)
        obj3 =  datetime.datetime.today() + datetime.timedelta(days=2)
        obj4 =  datetime.datetime.today() + datetime.timedelta(days=3)
        obj5 =  datetime.datetime.today() + datetime.timedelta(days=4)
        obj6 =  datetime.datetime.today() + datetime.timedelta(days=5)
       
           

        
        
        year1 = int(obj1.strftime("%Y"))
             #   print(year)
            #    print(type(year),"fgt")
        month1 =  int(obj1.strftime("%m"))
        day1 =  int(obj1.strftime("%d"))

        year2 = int(obj2.strftime("%Y"))
             #   print(year)
            #    print(type(year),"fgt")
        month2 =  int(obj2.strftime("%m"))
        day2 =  int(obj2.strftime("%d"))

        year3 = int(obj3.strftime("%Y"))
             #   print(year)
            #    print(type(year),"fgt")
        month3 =  int(obj3.strftime("%m"))
        day3 =  int(obj3.strftime("%d"))
 
        year4 = int(obj4.strftime("%Y"))
             #   print(year)
            #    print(type(year),"fgt")
        month4 =  int(obj4.strftime("%m"))
        day4 =  int(obj4.strftime("%d"))


        year5 = int(obj5.strftime("%Y"))
             #   print(year)
            #    print(type(year),"fgt")
        month5 =  int(obj5.strftime("%m"))
        day5 =  int(obj5.strftime("%d"))

        year6 = int(obj6.strftime("%Y"))
             #   print(year)
            #    print(type(year),"fgt")
        month6 =  int(obj6.strftime("%m"))
        day6 =  int(obj6.strftime("%d"))

        
        order_db11 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year1,month1,day1, 9 ,0,0) ).count()    
        order_db12 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year1,month1,day1, 10,0,0) ).count()    
        order_db13 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year1,month1,day1, 11 ,0,0) ).count()    
        order_db14 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year1,month1,day1, 12 ,0,0) ).count()    

        order_db21 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year2,month2,day2, 9 ,0,0) ).count()    
        order_db22 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year2,month2,day2, 10,0,0) ).count()    
        order_db23 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year2,month2,day2, 11 ,0,0) ).count()    
        order_db24 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year2,month2,day2, 12 ,0,0) ).count()
        
        order_db31 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year3,month3,day3, 9 ,0,0) ).count()    
        order_db32 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year3,month3,day3, 10,0,0) ).count()    
        order_db33 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year3,month3,day3, 11 ,0,0) ).count()    
        order_db34 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year3,month3,day3, 12 ,0,0) ).count()
        
        order_db41 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year4,month4,day4, 9 ,0,0) ).count()    
        order_db42 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year4,month4,day4, 10,0,0) ).count()    
        order_db43 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year4,month4,day4, 11 ,0,0) ).count()    
        order_db44 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year4,month4,day4, 12 ,0,0) ).count()
        
        order_db51 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year5,month5,day5, 9 ,0,0) ).count()    
        order_db52 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year5,month5,day5, 10,0,0) ).count()    
        order_db53 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year5,month5,day5, 11 ,0,0) ).count()    
        order_db54 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year5,month5,day5, 12 ,0,0) ).count()
        
        order_db61 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year6,month6,day6, 9 ,0,0) ).count()    
        order_db62 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year6,month6,day6, 10,0,0) ).count()    
        order_db63 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year6,month6,day6, 11 ,0,0) ).count()    
        order_db64 = Order.objects.filter(docname=user_name).filter(datetime_start= datetime.datetime(year6,month6,day6, 12 ,0,0) ).count()
        
        
        context['day1']=str(day1)+'/'+str(month1)+'/'+str(year1)
        context['day2']=str(day2)+'/'+str(month2)+'/'+str(year2)
        context['day3']=str(day3)+'/'+str(month3)+'/'+str(year3)
        context['day4']=str(day4)+'/'+str(month4)+'/'+str(year4)
        context['day5']=str(day5)+'/'+str(month5)+'/'+str(year5)
        context['day6']=str(day6)+'/'+str(month6)+'/'+str(year6)




        context['obj11']=5-order_db11
        context['obj12']=5-order_db12
        context['obj13']=5-order_db13
        context['obj14']=5-order_db14
        

        context['obj21']=5-order_db21
        context['obj22']=5-order_db22
        context['obj23']=5-order_db23
        context['obj24']=5-order_db24

        context['obj31']=5-order_db31
        context['obj32']=5-order_db32
        context['obj33']=5-order_db33
        context['obj34']=5-order_db34
        
        context['obj41']=5-order_db41
        context['obj42']=5-order_db42
        context['obj43']=5-order_db43
        context['obj44']=5-order_db44

        context['obj51']=5-order_db51
        context['obj52']=5-order_db52
        context['obj53']=5-order_db53
        context['obj54']=5-order_db54

        context['obj61']=5-order_db61
        context['obj62']=5-order_db62
        context['obj63']=5-order_db63
        context['obj64']=5-order_db64
        a=b=c=d=0

        price_obj=Doctor.objects.get(username=user_name)
        if '09:00-10:00' in price_obj.timeslots.values_list('name', flat=True):
            a=1
        if '10:00-11:00' in price_obj.timeslots.values_list('name', flat=True):
            b=1

        if '11:00-12:00' in price_obj.timeslots.values_list('name', flat=True):
            c=1

        if '12:00-13:00' in price_obj.timeslots.values_list('name', flat=True):
            d=1            

        print(price_obj.timeslots.values_list('name', flat=True))
       
        if obj1.isoweekday()==7:
            context['obj11']= context['obj12']= context['obj13']= context['obj14']=0

        if obj2.isoweekday()==7:
            context['obj21']= context['obj22']= context['obj23']= context['obj24']=0

        if obj3.isoweekday()==7:
            context['obj31']= context['obj32']= context['ob313']= context['obj34']=0

        if obj4.isoweekday()==7:
            context['obj41']= context['obj42']= context['obj43']= context['obj44']=0

        if obj5.isoweekday()==7:
            context['obj51']= context['obj52']= context['obj53']= context['obj54']=0

        if obj6.isoweekday()==7:
            context['obj61']= context['obj62']= context['obj63']= context['obj64']=0                    

        context['a']=a
        context['b']=b
        context['c']=c
        context['d']=d
        context['doctor']=doctor5
        
        return render(request,"appointment.html",context)



@login_required
def doctor(request):
    if request.method=='POST':
        form=DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            
            if Doctor.objects.filter(username = request.user.username).first():
                messages.success(request, 'You have already registered as a doctor')
                return render(request,"fail.html")
           
            post = form.save(commit=False)
            post.username = request.user.username
            post.save()
           
    
            
            selected_categories = form.cleaned_data.get('timeslots')
            for title in selected_categories:
              category_obj = Property.objects.get(name=title) #get object by title i.e I declared unique for title under Category model
              post.timeslots.add(category_obj) #now add each category object to the saved form object
            #users=Doctor.objects.all()
            context={}
            return redirect('/')
            
        else:
            return render(request,"fail.html")
    else:
        context={}
        context['form']=DoctorForm()
        return render(request,"doctor.html",context)

@login_required 
def display(request):
    context={}
    context['appointment']=Appointment.objects.all()
    return render(request,"display.html",context)


class DoctorListView(LoginRequiredMixin,generic.ListView):
    model = Doctor
    template_name = 'doctorList.html' 
    
    

class ProfileView( LoginRequiredMixin,View):
    def get(self, request, user_name):
        user_obj = Doctor.objects.get(username=user_name)
        print(user_obj.timeslots.values_list('name', flat=True))
       
        param = {'user_data':user_obj}
        return render(request, 'doctorprofile.html', param)


class ProfileViewPatient( LoginRequiredMixin,View):

    def get(self, request):
        user_obj = Patient.objects.get(username=request.user.username)
        
        
        param = {'user_data':user_obj}
        return render(request, 'patientprofile.html', param)


class DeleteCartView( LoginRequiredMixin,ListView):
    model = Cart
    def get(self, request, user_name):
        delete_post = self.model.objects.get(pk=user_name)
        
        delete_post.delete()
      





class DeleteView( LoginRequiredMixin,ListView):
    model = Doctor
    def get(self, request, user_name):
        delete_post = self.model.objects.get(pk=user_name)
        user2=delete_post.username
        print(delete_post.username)
        delete_post.delete()
        messages.success(request, 'Your post has been deleted successfully.')
        return redirect('/')


@login_required
def doctor_detail_view(request, primary_key):
    doctor = get_object_or_404(Doctor, pk=primary_key)
    return render(request, 'doctor_detail.html', context={'doctor': doctor})


def UploadViewPatient(request):
    if request.method=='POST':
        form=uploadForm(request.POST, request.FILES)
        if form.is_valid():
           
            post = form.save(commit=False)
            post.doctor = Doctor(username=request.user)
            post.save()
            patient_obj= Patient(username = post.patientUsername)
            patient_obj.save()
            patient_obj.prescription.add(post)
            
            return redirect('/')
        else:
            context={}
            context['form']=uploadForm(request.POST)
            return render(request,"fail.html",context)
    else:
        context={}
        context['form']=uploadForm()
        return render(request,"upload_file.html",context) 

@login_required 
def doctor_detail_view(request, user_name):
    try:
        doctor = Doctor.objects.get(pk=user_name)
    except Doctor.DoesNotExist:
        raise Http404('Doctor does not exist')

    return render(request, 'doctor_detail.html', context={'doctor': doctor})







@login_required 
def indexpay(request):
    currency = 'INR'
    
    
    
    cart = Cart.objects.get(username = request.user.username)
 
    amount=cart.price*100
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    
    order = Order.objects.create(user = request.user, total_amount = cart.price,razorpay_order_id = razorpay_order['id'])

    
  
    callback_url = f'/doctor/paymenthandler/'
    

	# we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    return render(request, 'indexpay.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.

# for generating pdf invoice



def fetch_resources(uri, rel):
    path = os.path.join(uri.replace(settings.STATIC_URL, ""))
    return path

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None




@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            order_db = Order.objects.get(razorpay_order_id= razorpay_order_id)
            # verify the payment signature.
            order_db.razorpay_payment_id = payment_id
            order_db.razorpay_signature = signature
            order_db.save()
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is None:
                cart = Cart.objects.get(username = request.user.username)
 
                amount=cart.price*100
                
                try:
                    order_db.payment_status = 1
                    order_db.save()
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    template = get_template('invoice.html')
                    patient_obj= Patient.objects.get(username= order_db.user.username)
                    name= patient_obj.name
                    doctor =  Cart.objects.get(username=request.user.username).docname
                    docprice =  Cart.objects.get(username=request.user.username).price
                    data = {
                        'order_id': order_db.order_id,
                        'transaction_id': order_db.razorpay_payment_id,
                        'user_email': order_db.user.email,
                        'date': str(order_db.datetime_of_payment),
                        'name': name,
                        'doctor':doctor,
                        'price':docprice,
                        'amount': order_db.total_amount,
                    }
                    html  = template.render(data)
                    result = BytesIO()
                    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
                    pdf = result.getvalue()
                    filename = 'Invoice_' + data['order_id'] + '.pdf'

                    mail_subject = 'Recent Order Details'
                    # message = render_to_string('firstapp/payment/emailinvoice.html', {
                    #     'user': order_db.user,
                    #     'order': order_db
                    # })

                    context_dict = {
                        'user': order_db.user,
                        'name':name,
                        'order': order_db
                    }

                    template = get_template('emailinvoice.html')
                    message  = template.render(context_dict)
                    to_email = order_db.user.email
                    c = Cart.objects.get(username=request.user.username)
                    c.order_id =  order_db.order_id
                    c.save()
                    order_db.docname = c.docname
                    order_db.datetime_start =c.datetime_start
                    order_db.datetime_end = c.datetime_end
                    order_db.save()

                    cart = Cart.objects.get(username = request.user.username)
                    
                    cart.delete()
                    try:
                        email = EmailMultiAlternatives(
                            mail_subject,
                            "hello",       # necessary to pass some message here
                            settings.EMAIL_HOST_USER,
                            [to_email]
                        )
                        email.attach_alternative(message, "text/html")
                        email.attach(filename, pdf, 'application/pdf')
                        email.send(fail_silently=False)
                        return render(request,'paymentsuccess.html')
                    except:
                        return render(request,'paymentsuccess.html')
                   
                    # render success page on successful caputre of payment
                   
                except:
                    order_db.payment_status = 2
                    order_db.save()
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
                order_db.payment_status = 2
                order_db.save()
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()





class GenerateInvoice(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            order_db = Order.objects.get(id = pk, user = request.user, payment_status = 1)     #you can filter using order_id as well
        except:
            return HttpResponse("505 Not Found")
        data = {
            'order_id': order_db.order_id,
            'transaction_id': order_db.razorpay_payment_id,
            'user_email': order_db.user.email,
            'date': str(order_db.datetime_of_payment),
            'name': order_db.user.name,
            'order': order_db,
            'amount': order_db.total_amount,
        }
        pdf = render_to_pdf('invoice.html', data)
        #return HttpResponse(pdf, content_type='application/pdf')

        # force download
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %(data['order_id'])
            content = "inline; filename='%s'" %(filename)
            #download = request.GET.get("download")
            #if download:
            content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

