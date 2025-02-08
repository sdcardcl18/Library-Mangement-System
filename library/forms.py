from django import forms
from django.contrib.auth.models import User
from .models import Student, BookIssued, Book


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'myAddclass','placeholder':'password..'}),required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'myAddclass','placeholder':'firstname..'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'myAddclass','placeholder':'lastname..'}),required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'myAddclass','placeholder':'username..'}),required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'myAddclass','placeholder':'email..'}),required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class StudentForm(forms.ModelForm):
    branch = forms.CharField(widget=forms.TextInput(attrs={'class':'myAddclass','placeholder':'Branch..'}),required=True)
    enrollment_number = forms.IntegerField(widget = forms.NumberInput(attrs={'class': 'myAddclass', 'placeholder':'Enrollment Number...'}),required=True)
    class Meta:
        model = Student
        fields = ('enrollment_number','branch')


class BookForm(forms.ModelForm):
    book_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'myAddclass', 'placeholder':'Book Name...'}),required=True)
    author_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'myAddclass', 'placeholder':'Author Name...'}),required=True)
    category = forms.CharField(widget = forms.TextInput(attrs={'class': 'myAddclass', 'placeholder':'Category...'}),required=True)
    isbn_number = forms.IntegerField(widget = forms.NumberInput(attrs={'class': 'myAddclass', 'placeholder':'Isbn Number...'}),required=True)
    class Meta:
        model = Book
        fields = '__all__'


class BookIssuedForm(forms.ModelForm):
    class Meta:
        model = BookIssued
        fields = '__all__'