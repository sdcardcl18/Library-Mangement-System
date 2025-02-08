from django.contrib.auth import views as auth_views
from django.urls import path
from library import views

app_name = 'library'

urlpatterns = [

    path('login_student_form/',views.studentLoginView,name='student_login_view'),
    path('login_student/',views.studentLogin,name='student_login'),
    path('login_librarian_form/',views.librarianLoginView,name='librarian_login_view'),
    path('login_librarian/',views.librarianLogin,name='librarian_login'),
    path('register_as_a_student/',views.registerationView,name='register'),
    path('books_list/',views.bookList,name='books_list_view'),
    path('logout/',views.userLogout,name='user_logout'),
    path('student_report/',views.studentReportView,name='student_report_view'),
    path('add_books/',views.addBooksView,name='add_books_view'),
    path('books_issued/',views.issuedBooksView,name='books_issued_view'),
    path('about/',views.aboutView,name='about_view'),
    path('delete_book/<int:pk>/remove/',views.deleteBook,name='delete_book_row'),
    path('update_book/<int:pk>/update/',views.updateBook,name='update_book_row'),
    path('issue_book/<int:pk>/issue/',views.issueBook,name='issue_book'),
    path('search_book/',views.searchBook,name='search'),
    path('login/',views.loginView,name='login'),
    path('return_book/<int:pk>/return/',views.returnIssued,name='return_book'),
    path('update_student/<int:pk>/update_student_details/',views.updateStudent,name='update_student'),
    path('delete_student/<int:pk>/remove_student/',views.deleteStudent,name='delete_student'),
    
]
