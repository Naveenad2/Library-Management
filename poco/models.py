from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Section(models.Model):

    sectoin_name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to="./static/images")

    def __str__(self) :
        return self.sectoin_name


class Books(models.Model):

    connection =models.ForeignKey(Section,on_delete=models.CASCADE)

    book_name = models.CharField(max_length=50)
    discription = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="./static/images")
    author_name = models.CharField(max_length=40)
    page_number = models.IntegerField()
    
    def __str__(self) :
        return self.book_name

class Student(models.Model):

    connection = models.OneToOneField(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=200,null=True)
    phone_number = models.ImageField()
    school = models.CharField(max_length=200,null=True)
    class_name = models.CharField(max_length=40,null=True)


    def __str__(self) :
        return self.name
    


class Librarian(models.Model):
     
    connection = models.OneToOneField(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=200,null=True)
    phone_number = models.ImageField()



    def __str__(self) :
        return self.name

class Assign_Books_to_Students(models.Model):

    Select_a_student = models.ForeignKey(User,on_delete=models.CASCADE)
    Select_a_book = models.ForeignKey(Books,on_delete=models.CASCADE)

    start_date = models.CharField(max_length=40)

    due_date = models.CharField(max_length=40)


    def __str__(self) :
        return self.Select_a_student.username

    


