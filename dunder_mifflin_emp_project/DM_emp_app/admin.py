from django.contrib import admin
from DM_emp_app.models import Employee,Department,Role

# Register your models here.

admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)