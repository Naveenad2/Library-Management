from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def index(request):

    
    if (request.user.id is not None):
        
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if(Student.objects.filter(name = user.username).exists()):
             
             return redirect("/StudentMainPage")
        
        if(Librarian.objects.filter(name = user.username).exists()):
             
             return redirect("/LibrarianMainPage")
        
    elif(request.user.id==1):
       
       return redirect("/admin")
    
    else:

       return render(request,'main.html')
   

def Sregistration(request):
    return render(request,"Sregistration.html")

def Studen_auth(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    phno=request.POST.get('phno')
    address=request.POST.get('address')
    class_name=request.POST.get('cname')
    school=request.POST.get('school')

    password=request.POST.get('password')
    repeatpass=request.POST.get('repassword')

    if password == repeatpass:

        user = User.objects.filter(username=name)
        isuser = user.exists()
        if isuser is False:
            new_user = User.objects.create_user(username=name,password=password)
            new_user.save()


                #save the user
            employee = Student(
            connection =new_user,
            name=name,
            school=school,
           
            class_name=class_name,
            email=email,
            phone_number=phno,
            address=address )
            
            employee.save()

            authuser = authenticate(username=name,password=password)
            login(request,authuser)

    else:
        return render(request,'Studen_registration.html')

    
    return redirect('/StudentMainPage')

def Slogin(request):
    return render(request,"Slogin.html")


# librarian registration
def librarian_registration(request):
    return render(request,"librarian_registration.html")

def librarian_auth(request):

    name=request.POST.get('name')
    email=request.POST.get('email')
    phno=request.POST.get('phno')
    address=request.POST.get('address')

    password=request.POST.get('password')
    repeatpass=request.POST.get('repassword')

    if password == repeatpass:

            user = User.objects.filter(username=name)
            isuser = user.exists()
            if isuser is False:
                new_user = User.objects.create_user(username=name,password=password, is_superuser =True,is_active = True,is_staff = True )
                new_user.save()


                #save the user
                librarian = Librarian(
                connection =new_user,
                name=name,
                
                email=email,
                phone_number=phno,
                address=address)
                
                librarian.save()

                authuser = authenticate(username=name,password=password)
                login(request,authuser)

    else:
        return render(request,'librarian_registration.html')

    
    return redirect('/LibrarianMainPage')

def Studen_registration(request):
    return render(request,"Studen_registration.html")

def Student_login(request):

    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('StudentMainPage')
        else:
            return HttpResponse("Wrong password")
        
    return render(request,"Student_login.html")
   

def librarian_login(request):

     if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/LibrarianMainPage')
        else:
            return HttpResponse("Wrong password")
        
     return render(request,"librarian_login.html")




def StudentMainPage(request):

    section = Section.objects.all()

    return render(request,"StudentMainPage.html",{"section":section})


def StudentBookView(request,id):
     
     section_obj = Section.objects.get(id = id)
     books = Books.objects.filter(connection=section_obj)
     

     return render(request,"StudentBookView.html",{"books":books})

def ViewAllBooks(request):
     books = Books.objects.all()

     return render(request,"StudentBookView.html",{"books":books})


def search_books_by_name(request):
      username = request.POST.get('book')
      query = Q(book_name__icontains=username)

        # Perform the search using the filter() method on the model's manager
      books = Books.objects.filter(query)
     
      return render(request,"StudentBookView.html",{"books":books})


def search_books_by_Authoname(request):
     username = request.POST.get('book')
     query = Q(author_name__icontains=username)

        # Perform the search using the filter() method on the model's manager
     books = Books.objects.filter(query)

     return render(request,"StudentBookView.html",{"books":books})


def LibrarianMainPage(request):
    section = Section.objects.all()

    return render(request,"LibrarianMainPage.html",{"section":section})


def LibrarianBookView(request,id):
     
     section_obj = Section.objects.get(id = id)
     books = Books.objects.filter(connection=section_obj)

     return render(request,"LibrarianBookView.html",{"books":books})


def LibrarianViewbookDetails(request,id):

    book_obj = Books.objects.get(id = id)


    return render(request,"LibrarianViewbookDetails.html",{"book_obj":book_obj})

def EditBooks(request,id):

    book_obj = Books.objects.get(id = id)

    return render(request,"EditBooks.html",{"book_obj":book_obj})


def ViewBook(request,id):

    book_obj = Books.objects.get(id = id)

    return render(request,"view_book.html",{"book_obj":book_obj})


def saveBookChanges(request):

     name=request.POST.get('name')
     aname=request.POST.get('aname')
     discription=request.POST.get('discription')
     pno=request.POST.get('pno')

     id=request.POST.get('id')

     book_obj = Books.objects.get(id = id)

     book_obj.book_name = name
     book_obj.author_name = aname
     book_obj.discription = discription
     book_obj.page_number = pno

     book_obj.save()


   

     return redirect(f"LibrarianViewbookDetails/{id}")




def viewStudents(request):

    studets = Student.objects.all()

    return render(request,"viewStudents.html",{"studets":studets})


def AddBooksToStudents(request,id):

    studentsid = id

    books = Books.objects.all()

    return render(request,"AddBooksToStudents.html",{"studentsid":studentsid,"books":books})


def AddBooksToStudentsImplemetation(request,id,id2):
   
       studentsid = id2
       bookid = id

       books = Books.objects.get(id=bookid)    
        
       return render(request,"AddBooksToStudentsImplemetation.html",{"studentsid":studentsid,"bookid":bookid,"books":books})



def SelectBooksToAddToStudents(request):

    if request.method == 'POST':
        stime = request.POST.get('stime')
        etime = request.POST.get('etime')

        studentsid = request.POST.get('studentsid')
        bookid = request.POST.get('bookid')

        student_obj = User.objects.get(id=studentsid)
        book_obj = Books.objects.get(id=bookid)

        a_object = Assign_Books_to_Students(
            Select_a_student = student_obj,
            Select_a_book = book_obj,
            start_date = stime,
            due_date = etime
        )
        a_object.save()

        return redirect("/viewStudents")
    
def ViewAssaignedBooks(request,id):

    student_obj = User.objects.get(id=id)
    books = Assign_Books_to_Students.objects.filter(Select_a_student=student_obj)

    return render(request,"ViewAssaignedBooks.html",{"books":books})



def ViewsStudentsBooksByStudents(request):

    id = request.user.id

    u = id - 1

    student_obj = User.objects.get(id=id)
    books = Assign_Books_to_Students.objects.filter(Select_a_student=student_obj)
    return render(request,"ViewsStudentsBooksByStudents.html",{"books":books})
      


def Logout_(request):
       logout(request)
       return redirect("/")
  