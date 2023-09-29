from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # make sure widget is after max_length; if you are not sure about positions of the argumnets passed, just hover over "Charfield" or "EmailField" or whatever and it will show you the arguments that are passed, write your arguments accordingly.
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2'] # Use list or set not dict. List and set will give the elements to show up in order as they are placed, while dict will jumble up the order
        # password1 and password2 are the names Django assigned to the password field in the registration form. On for entering a password and other is for confirmation
    
    # This is to add bootstrap to the inherited field from UserCreationForm. Read documentation about "widgets" to know more.
    def __init__(self, *args: Any, **kwargs: Any):
        super(SignUpForm,self).__init__(*args, **kwargs) #This code is defining a special method called __init__ that is used when creating a new instance of the SignUpForm class. When this method is called, it first calls the __init__ method of the parent class UserCreationForm using the super() function.
        
        
        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['password1'].widget.attrs['class'] ='form-control'
        self.fields['password2'].widget.attrs['class'] ='form-control'
        # this method modifies some of the form fields by adding a CSS class to their HTML widget. Specifically, it adds the class form-control to the widgets for the username, password1, and password2 fields.
        
class EditProfileForm(UserChangeForm):
    # There are lot of things in UserChangeForm form, if you want to see all of them, replace the "EditProfileForm" with "UserChangeForm" in the "form_class" in UserEditView class in "views.py" file.
    
    # To add bootstrap to checkboxes use "form-check" instead of "form-control" in the attrs class
    
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']