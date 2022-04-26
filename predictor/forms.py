from django import forms
from .models import HeartData

GENDER_CHOICES = (('-','Select an Option'),(1,'Male'),(0,'Female'))

CHOICES = (('-','Select an Option'),(1,'Yes'),(0,'No'))

class Parameters(forms.Form):
    age = forms.IntegerField(max_value=120,min_value=1 , widget=forms.NumberInput(attrs={'id':'a1' , 'type':'text','class':'validate'}) , error_messages={'invalid':'Please enter a number'})
    gender= forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}))
    activity= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}))
    rest= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}))
    night= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}))
    exercise= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}))
    diabetes= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}))
    
    dquestion1= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}),required=False)
    dquestion2= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}),required=False)
    dquestion3= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}),required=False)
    dquestion4= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}),required=False)
    
    bp= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}))
    
    bpquestion1= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}),required=False)
    bpquestion2= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}),required=False)
    bpquestion3= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}),required=False)
    bpquestion4= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}),required=False)
    
    cyanosis= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}))
    clubbing= forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'validate','required': 'true'}))
    
