from django.urls import path
from api import views

urlpatterns = [
    path('',views.student_list),
    path('details/<int:num>/',views.student_details),
    path('create/',views.student_create),
    path('update/<int:num>/',views.student_update),
    path('delete/<int:num>/',views.student_delete),
]