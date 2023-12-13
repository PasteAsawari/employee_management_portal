from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name+"-"+self.location

class Role(models.Model):
    pos_name = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.pos_name
    

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=10,primary_key=True,default="E100")

    def save(self,*args,**kwargs):
        if not self.employee_id.startswith("E"):
            self.employee_id = "E"+self.employee_id
        super().save(*args,**kwargs)

    first_name = models.CharField(max_length=100,null=False)
    last_name= models.CharField(max_length=100)
    email_id = models.EmailField(max_length=150,null=False)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return self.employee_id+"-"+self.first_name