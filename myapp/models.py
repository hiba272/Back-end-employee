from django.db import models



class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    document = models.FileField(upload_to='documents/', blank=True, null=True)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
