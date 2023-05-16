from django.urls import path

from Main import views

app_name="Main"

urlpatterns = [
    path("",views.student_list, name="student_data"),

]