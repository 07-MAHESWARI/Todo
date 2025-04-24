from django.db import models

# Create your models here.

from django.contrib.auth.models import User # imported the UserAuth for User table

# AbstractUser is a class we can use for creating user table with our needed fields


class TaskModel(models.Model):  # Task table

    taskname= models.CharField(max_length=100)

    created_date = models.DateField(auto_now=True)
    # yyyy-mm-dd

    due_date = models.DateField()

    description = models.TextField()

    category = [
        ("work","work"),
        ("personal","personal"),
        ("urgent","urgent")

    ]  # tuple --> two (one for label and other for db)
    task_category = models.CharField(max_length=50,choices=category)

    complete_status = models.BooleanField(default=False)

    user_id = models.ForeignKey(User, on_delete= models.CASCADE)   #foreign key : id of user table is foreign key of task table
                                                                   # by default the relation is one to many 

    def __str__(self):
        return self.taskname     # for understanding in client side(we can give any str obj field of the class)
    


class OTPModel(models.Model):

    user_id = models.ForeignKey(User, on_delete = models.CASCADE)   # one to many (always)

    otp = models.CharField(max_length=100)

    created_at = models.DateField(auto_now_add=True)
