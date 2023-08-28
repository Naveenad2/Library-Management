"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
   path('',views.index,name='index'),
   path('Sregistration',views.Sregistration,name="Sregistration"),
   path('Slogin',views.Slogin,name="Sregistration"),

   path('librarian_registration',views.librarian_registration,name="librarian_registration"),
   path('librarian_auth',views.librarian_auth,name="librarian_auth"),

   path('Studen_registration',views.Studen_registration,name="Studen_registration"),
   path('Studen_auth',views.Studen_auth,name="Studen_auth"),

   path('Student_login',views.Student_login,name="Student_login"),
   path('librarian_login',views.librarian_login,name="librarian_login"),

   path('StudentMainPage',views.StudentMainPage,name="StudentMainPage"),
   path('LibrarianMainPage',views.LibrarianMainPage,name="LibrarianMainPage"),

   path('StudentBookView/<int:id>',views.StudentBookView,name="StudentBookView"),
   path('LibrarianBookView/<int:id>',views.LibrarianBookView,name="LibrarianBookView"),

    path('EditBooks/<int:id>',views.EditBooks,name="EditBooks"),
    path('saveBookChanges',views.saveBookChanges,name="saveBookChanges"),

    path('ViewBook/<int:id>',views.ViewBook,name="ViewBook"),
    path('LibrarianViewbookDetails/<int:id>',views.LibrarianViewbookDetails,name="LibrarianViewbookDetails"),


    path('viewStudents',views.viewStudents,name="viewStudents"),

    path('AddBooksToStudents/<int:id>',views.AddBooksToStudents,name="AddBooksToStudents"),
    path('AddBooksToStudentsImplemetation/<int:id>/<int:id2>',views.AddBooksToStudentsImplemetation,name="AddBooksToStudentsImplemetation"),

    path('SelectBooksToAddToStudents',views.SelectBooksToAddToStudents,name="SelectBooksToAddToStudents"),

     path('ViewsStudentsBooksByStudents',views.ViewsStudentsBooksByStudents,name="ViewsStudentsBooksByStudents"),

     path('ViewAssaignedBooks/<int:id>',views.ViewAssaignedBooks,name="ViewAssaignedBooks"),
     path('search_books_by_name',views.search_books_by_name,name="search_books_by_name"),
      path('search_books_by_Authoname',views.search_books_by_Authoname,name="search_books_by_Authoname"),
      path('ViewAllBooks',views.ViewAllBooks,name="ViewAllBooks"),


    path('logout',views.Logout_,name="Logout_"),




]

