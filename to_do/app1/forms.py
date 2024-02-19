from django import forms 

class Userform(forms.Form):
      user_name = forms.CharField(max_length=100,label="User Name")
      email = forms.EmailField(label="Email Id" )
      password = forms.CharField(label="Password")
      
    
