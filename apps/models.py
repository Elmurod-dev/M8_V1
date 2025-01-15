from django.db.models import Model, CharField, EmailField, DateTimeField, TextField, ForeignKey, CASCADE


# from django.db import models
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     pages = models.IntegerField()
#
#     def __str__(self):
#         return self.title
#



# Homework
class CustomUsers(Model):
    username = CharField(max_length=255)
    email = EmailField(max_length=255,unique=True)
    password = CharField(max_length=255)
    date_joined = DateTimeField(auto_now_add=True)


class Post(Model):
    title = CharField(max_length=255)
    description = TextField()
    user = ForeignKey('apps.CustomUsers',CASCADE,related_name='posts')
