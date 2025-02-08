from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    student = models.OneToOneField(User,on_delete=models.CASCADE)
    enrollment_number = models.PositiveIntegerField()
    branch = models.CharField(max_length=500)

    def __str__(self):
        return self.student.firstname


class Book(models.Model):
    book_name = models.CharField(max_length=300)
    author_name = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    isbn_number = models.PositiveIntegerField()

    def __str__(self):
        return self.book_name


class BookIssued(models.Model):
    book_name = models.CharField(max_length=300)
    author_name = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    isbn_number = models.PositiveIntegerField()
    issued_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name
