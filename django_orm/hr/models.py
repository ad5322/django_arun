from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=50,unique=True,null=True)
    address = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.phone

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    
    contact = models.OneToOneField(Contact,on_delete=models.CASCADE,null=True)
    
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
