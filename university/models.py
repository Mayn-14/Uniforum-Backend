from django.db import models
from customUser.models import Account

class School(models.Model):
    school_name = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name

class Programme(models.Model):
    programme_name = models.CharField(max_length=100)
    duration = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.programme_name

class Student(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='studentDetail')
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=100)
    semester = models.IntegerField(null=True)
    batch = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.roll_no

    
