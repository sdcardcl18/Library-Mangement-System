from django.contrib.auth.models import User
from library.models import Book, BookIssued, Student
from library.forms import UserForm, StudentForm, BookForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

# Home Page
@login_required(login_url='library:login')
def bookList(request):
    user = request.user
    books = Book.objects.all()
    books_count = Book.objects.count()
    context = {'books':books,'books_count':books_count,'user':user}
    return render(request,'library/book_list.html',context)


# Login page
def loginView(request):
    return render(request,'library/login.html')


# Student login View
def studentLoginView(request):
    return render(request,'library/login_student.html')


# Student Login
def studentLogin(request):

    flag = True
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect(reverse('library:books_list_view')) # booklist is the main page
            else:
                return HttpResponse("Account Not Active")
        else:
            flag = False
            return render(request,'library/login_student.html',{'flag':flag})

    else:
        return render(request,'library/login.html')


# Admin Login
def librarianLogin(request):

    flag = True
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect(reverse('library:books_list_view')) # booklist is the main page
            else:
                return HttpResponse("Account Not Active")
        else:
            flag = False
            return render(request,'library/login_student.html', {'flag': flag})

    else:
        
        return render(request,'library/login.html')


# Logout
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse(loginView))


# Librarian login
def librarianLoginView(request):
    return render(request,'library/login_librarian.html')


# Register
def registerationView(request):

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)  # getting the whole data from the user.
        student_form = StudentForm(data=request.POST)

        if user_form.is_valid() and student_form.is_valid():

            user = user_form.save()
            user.set_password(user.password) # creates a hashed password
            user.save()

            student = student_form.save(commit=False)
            student.student = user
            student.save()

            return redirect('library:student_login_view') # redirect to login page
        else:
            print(user_form.errors,student_form.errors)

    else:
        user_form = UserForm()
        student_form = StudentForm()

    context = {'user_form':user_form, 'student_form':student_form}

    return render(request,'registration/register.html',context)


# Student Report View
@login_required(login_url='library:login')
def studentReportView(request):
    
    users = User.objects.filter(is_superuser=False).order_by('id')
    users_count = User.objects.filter(is_superuser=False).count()
    students = Student.objects.all()

    userstud = {}
    for i in range(users_count):

        userstud[i] = {}
    # 

    i = 0
    for u, s in zip(users, students):

        userstud[i]['id'] = u.id
        userstud[i]['first_name'] = u.first_name
        userstud[i]['last_name'] = u.last_name
        userstud[i]['email'] = u.email
        userstud[i]['enrollment_number'] = s.enrollment_number
        userstud[i]['branch'] = s.branch

        i = i + 1

    print(userstud)

    context = {'userstud': userstud}
    return render(request,'library/student_report.html',context)
    

# Add books view
@login_required(login_url='library:login')
def addBooksView(request):

    flag = False
    if request.method == 'POST':

        book_form = BookForm(data=request.POST) 

        if book_form.is_valid():
            book_form.save()
            book_form = BookForm()
            flag = True
        else:
            print(book_form.errors())

    else:

        book_form = BookForm()

    context = {'book_form':book_form,'flag':flag}

    return render(request,'library/add_books_page.html',context)


# Issued books view
@login_required(login_url='library:login')
def issuedBooksView(request):
    issuedbooks = BookIssued.objects.filter(student_id=request.user.id)
    context = {'issuedbooks':issuedbooks,}
    return render(request,'library/books_issued.html',context)


# About view
def aboutView(request):
    return render(request,'library/about.html')


# Delete book record
def deleteBook(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('library:books_list_view')


# Update a Book details
def updateBook(request,pk):

    book = Book.objects.get(pk=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library:books_list_view')

    return render(request,'library/update_book_details.html',{'form':form})


# Issue a book
def issueBook(request,pk):

    user = request.user
    book = Book.objects.get(pk=pk)
    
    # assign values to the bookissued class object
    bookissued = BookIssued()
    bookissued.book_name = book.book_name
    bookissued.author_name = book.author_name
    bookissued.category = book.category
    bookissued.isbn_number = book.isbn_number

    bookissued.student_id = user.id

    bookissued.save()
    book.delete()

    return redirect('library:books_list_view')


# Search functionality
def searchBook(request):
    
    if request.method == 'GET':      
        book_name =  request.GET.get('search')      
        try:
            status = Book.objects.filter(book_name__icontains=book_name)
        except Book.DoesNotExist:
            status = None
        return render(request,'library/book_list.html',{'filteredbooks':status})
    else:
        return render(request,'library/book_list.html',{})


# Return issued books
def returnIssued(request,pk):

    bookissued = BookIssued.objects.get(pk=pk)

    book = Book()
    book.book_name = bookissued.book_name
    book.author_name = bookissued.author_name
    book.category = bookissued.category
    book.isbn_number = bookissued.isbn_number

    book.save()
    bookissued.delete()

    return redirect('library:books_issued_view')


# Update Student Details
def updateStudent(request, pk):

    user = User.objects.get(pk=pk)
    userForm = UserForm(instance=user)
    student = Student.objects.get(student_id=pk)
    studentForm = StudentForm(instance=student)

    if request.method == 'POST':

        userForm = UserForm(data=request.POST, instance=user)
        studentForm = StudentForm(data=request.POST, instance=student)

        if userForm.is_valid() and studentForm.is_valid():
            user = userForm.save()
            user.set_password(user.password) # creates a hashed password
            user.save()

            studentForm.save()
            return redirect('library:student_report_view')

    context = {'userForm':userForm,'studentForm':studentForm}
    
    return render(request,'library/student_update.html',context)


# Delete Student
def deleteStudent(request, pk):
    user = User.objects.filter(pk=pk)
    user.delete()
    return redirect('library:student_report_view')

