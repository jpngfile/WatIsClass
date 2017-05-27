
from django import forms
from django.forms import ModelForm


class RoomForm(ModelForm):
    course = forms.CharField(label='Room Code', max_length=10)


class CourseForm(forms.Form):
    course = forms.CharField(label='Course Name', max_length=100, widget=forms.TextInput(attrs=
    	{'class': "form-control", 'id': "className", 'placeholder': "Class name"}))
    num_lectures = forms.IntegerField(label='Number of Lectures', widget=forms.NumberInput(attrs=
    	{'class': "form-control", 'id': "numPages", 'placeholder': "Number of Pages"}))

