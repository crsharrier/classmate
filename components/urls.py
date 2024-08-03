from django.urls import path
from . import views
from components.classes_widget.classes_widget import StudentList

urlpatterns = [
    path('student_list/', StudentList.as_view()),
    path('selected-class/', views.SelectedClassView.as_view()),
]
