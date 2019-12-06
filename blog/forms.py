from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import Book, Rsvp, Rsvp_template

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title', 'name', 'image')

class RsvpForm(forms.ModelForm):
	class Meta:
		model = Rsvp
		fields = ('name', 'address', 'city', 'state', 'zip_code', 'email')

class RsvpTemplateForm(forms.ModelForm):
	class Meta:
		model = Rsvp_template
		fields = ('title', 'image')



# class UserRegisterForm(UserCreationForm):
# 	email = forms.EmailField()

# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password1', 'password2']

# class UserUpdateForm(forms.ModelForm):
# 	email = forms.EmailField()

# 	class Meta:
# 		model = User
# 		fields = ['username', 'email']

# class ProfileUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model = Profile
# 		fields= ['image']