from django.shortcuts import render, HttpResponse
from .models import Employee,Department,Role
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,"index.html")

def allEmp(request):
    employees = Employee.objects.all()
    context = {
        "employees" : employees
    }
    return render(request,"allEmp.html",context)



def addEmp(request):
    if request.method == "POST":
        emp_id = request.POST.get("employeeId","")
        fname = request.POST.get("fname","")
        lname = request.POST.get("lname","")
        email_id = request.POST.get("email_id","")
        phone = request.POST.get("phone","")
        dept= request.POST.get("edepartment","")
        role = request.POST.get("erole","")
        salary = request.POST.get("salary","")
        bonus = request.POST.get("bonus","")
        print(emp_id,fname,lname,email_id,phone,dept,role,salary,bonus)
        new_employee = Employee(employee_id=emp_id,first_name=fname,last_name=lname,email_id=email_id,phone=phone,dept=Department.objects.get(dept_name=dept),role=Role.objects.get(pos_name=role),salary=salary,bonus=bonus,hire_date=datetime.now())
        new_employee.save()
        return HttpResponse("Employee has been added Sucessfully!")
    elif request.method == "GET":
        depts = Department.objects.all()
        roles = Role.objects.all()
        context = {
            "depts":depts,
            "roles":roles
        }
        
        
        return render(request,"addEmp.html",context)
    else:
        return HttpResponse("Error has occured! Employee has not been Added!")

def removeEmp(request,emp_id=None):
    if emp_id:
        try:
            employee_to_be_removed = Employee.objects.get(employee_id =emp_id)
            employee_to_be_removed.delete()
            return HttpResponse("Employee has been deleted sucessfully!")
        except:
            return HttpResponse("Invalid Employee ID!! Failed to remove the employee!!")
    emps = Employee.objects.all()
    context ={
        "emps":emps
    }
    return render(request,"removeEmp.html",context)

def filterEmp(request):
    if request.method =="POST":
        name = request.POST.get("name","")
        dept = request.POST.get("dept","")
        role =request.POST.get("role","")
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains= name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__dept_name__icontains = dept)
        if role:
            emps = emps.filter(role__pos_name__icontains=role)
        context={
            "employees": emps
        }
        return render(request,"allEmp.html",context)
    

    elif request.method =="GET":
        return render(request,"filterEmp.html")
    else:
        return HttpResponse("Some error occured!!")
