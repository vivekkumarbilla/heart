from django.shortcuts import render,redirect
from sklearn import linear_model
from .forms import Parameters
from .regressor import LogitRegression
import pandas as pd
import numpy as np
from . import regressor
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression 
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login 
from django.contrib.auth.decorators import login_required
from .models import HeartData,DoctorHospital
from django.core.mail import send_mail
import pickle
# Create your views here.


model = pickle.load(open('model.pkl' , 'rb'))

def quickpredict(request):  #Predicts the results after form is submitted.Works only if user is not authenticated
    
    if request.method=='POST':
        print(request.POST)
        form=Parameters(request.POST)
        if form.is_valid():
            print('valid form')
            Age = form.cleaned_data['age']
            Gender = int(form.cleaned_data['gender'])
            Activity = int(form.cleaned_data['activity'])
            Rest = int(form.cleaned_data['rest'])
            Night = int(form.cleaned_data['night'])
            Exercise = int(form.cleaned_data['exercise'])
            Cyanosis = int(form.cleaned_data['cyanosis'])
            Diabetes = int(form.cleaned_data['diabetes'])
            if (Diabetes==0):
                dia1 = int(form.cleaned_data['dquestion1'])
                dia2 = int(form.cleaned_data['dquestion2'])
                dia3 = int(form.cleaned_data['dquestion3'])
                dia4 = int(form.cleaned_data['dquestion4'])
                if( dia1 + dia2 + dia3 + dia4 >=2 ):
                    Diabetes = 1
                else :
                    Diabetes = 0 
            bp = form.cleaned_data['bp']
            print(type(Diabetes),type(Activity))
            if(bp==0):
                bp1 = int(form.cleaned_data['bpquestion1'])
                bp2 = int(form.cleaned_data['bpquestion2'])
                bp3 = int(form.cleaned_data['bpquestion3'])
                bp4 = int(form.cleaned_data['bpquestion4'])
                if( bp1 + bp2 + bp3 + bp3 >=2 ):
                    bp = 1
                else :
                    bp = 0  
            clubbing = int(form.cleaned_data['clubbing'])

            output = model.predict([[Age,Gender,Activity,Rest,Night,Exercise,Cyanosis,Diabetes,bp,clubbing]])   
            
            output1 = 'high'  if output == 1 else 'low'
            return render(request , 'output.html' , {'output1':output1})
        else:
            print('The form was not valid.')
            return render(request,'quickpredict.html',{'form':form,'error': 'Please Enter all attributes correctly'})
        
        
    else:
        form=Parameters()
        return render(request,'quickpredict.html',{'form':form})

def index(request): #Directs the user to home page . Different for authenticated and non authenticated users.
    if request.user.is_authenticated:
        if request.method=='POST':
    
            form=Parameters(request.POST)
            if form.is_valid():
                Age = form.cleaned_data['age']
                Gender = int(form.cleaned_data['gender'])
                Activity = int(form.cleaned_data['activity'])
                Rest = int(form.cleaned_data['rest'])
                Night = int(form.cleaned_data['night'])
                Exercise = int(form.cleaned_data['exercise'])
                Diabetes = int(form.cleaned_data['diabetes'])
                if (Diabetes==0):
                    dia1 = int(form.cleaned_data['dquestion1'])
                    dia2 = int(form.cleaned_data['dquestion2'])
                    dia3 = int(form.cleaned_data['dquestion3'])
                    dia4 = int(form.cleaned_data['dquestion4'])
                    if( dia1 + dia2 + dia3 + dia4 >=2 ):
                        Diabetes = 1
                    else :
                        Diabetes = 0 
                bp = form.cleaned_data['bp']
                print(type(Diabetes),type(Activity))
                if(bp==0):
                    bp1 = int(form.cleaned_data['bpquestion1'])
                    bp2 = int(form.cleaned_data['bpquestion2'])
                    bp3 = int(form.cleaned_data['bpquestion3'])
                    bp4 = int(form.cleaned_data['bpquestion4'])
                    if( bp1 + bp2 + bp3 + bp4 >=2 ):
                        bp = 1
                    else :
                        bp = 0  
                Cyanosis = int(form.cleaned_data['cyanosis'])
                clubbing = int(form.cleaned_data['clubbing'])

                output = model.predict([[Age,Gender,Activity,Rest,Night,Exercise,Cyanosis,Diabetes,bp,clubbing]])   

                output1 = 'high'  if output == 1 else 'low'
                saved_data = HeartData(age=Age , 
                    gender = Gender,
                    activity = Activity,
                    rest = Rest,
                    night = Night,
                    exercise = Exercise,
                    diabetes = Diabetes,
                    bp = bp,
                    cyanosis = Cyanosis,
                    clubbing = clubbing,
                    owner = request.user,
                    probability = 100   if output == 1 else 0
                ) 
                 # Saved the authenticated users data in the database.
                saved_data.save()
                return render(request , 'output2.html',{'output1':output1 , 'danger':output1})

            else:
                print('The form was not valid.')
                return render(request,'user.html',{'form':form,'error': 'Please Enter all attributes correctly'})

        form = Parameters()
        return render(request , 'user.html', {'form':form})
    return render(request , 'index.html')



def record(request): #Diplays previous record of authenticated user
    if request.user.is_authenticated:
        record_data = HeartData.objects.filter(owner = request.user) #Filter only those data whose owner is the logged in user
        return render(request , 'record.html' , {'record_data':record_data})
    return redirect('/')

def heartdetail(request): # Displays previous results in detail
    if request.user.is_authenticated:
        record_data = HeartData.objects.filter(owner = request.user)
        return render(request , 'heartdetail.html' , {'record_data':record_data})
    return redirect('/')

def symptoms(request): # Diplays list of symptoms of heart disease
    if request.user.is_authenticated:
        record_data = HeartData.objects.all()
        return render(request , 'symptoms.html')
    return redirect('/')

def prevention(request): # Diplays list of prevention of heart disease
    if request.user.is_authenticated:
        return render(request , 'prevention.html')
    return render('/')

def doctorhospital(request): # Displays list of doctors and hospitals for user
    if request.user.is_authenticated:
        datas = DoctorHospital.objects.all()
        return render(request , 'doctorshospitals.html',{'datas':datas})
    return render('/')

def contact(request): #Diplays contact page . Sends email  using SMTP.
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title1')
        message = request.POST.get('message')
        
        send_mail(title , message+'\n'+'From : '+name+'\n'+'Email : '+email ,from_email=email, recipient_list=['heart.projectkj@gmail.com']) #Sends mail 
    return render(request , 'contact.html')



def about(request): #Displays about us page.
    return render(request , 'about.html')

# Login and Logout





def signin(request): # For the user to sign in.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'Invalid Credentials')
            return redirect('signin')

        
    else:
        return render(request,'signin.html')


def signup(request): #For the user to resister or sign up.

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, password=password,email=email,first_name = first_name,last_name=last_name)
            
            user.save()
            
            messages.success(request,f"User {username} created!")
            return redirect('signin')
        #return redirect('/')
    else:   
        return render(request,'signup.html')


def signout(request): # In order to logout from the website
    auth.logout(request)
    return redirect('/')


# End login