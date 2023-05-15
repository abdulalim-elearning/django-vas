from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, blank=True,  null=True)
    contact = models.IntegerField(default=0)
    bio = models.TextField()
    height = models.FloatField(default=2)

    def __str__(self):
        return self.bio


class Person(models.Model):
    name = models.CharField(max_length=100)

class Contact(models.Model):
    p = models.OneToOneField(Person, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)


class Student1(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student1)