
from django.urls import path
from DM_emp_app import views

#adding app's urlpatterns
urlpatterns = [
    path('',views.index, name="index"),
    path('allEmp',views.allEmp, name="allEmp"),
    path('addEmp',views.addEmp, name="addEmp"),
    path('removeEmp',views.removeEmp, name="removeEmp"),
    path('removeEmp/<str:emp_id>',views.removeEmp, name="removEmp"),
    path('filterEmp',views.filterEmp, name="filterEmp")
       
]
