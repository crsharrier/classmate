from typing import Optional
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django_components import component
from django.db.models import Max, Subquery, OuterRef
from classmate.models import Class, ClassAssignment, Student


def get_students_by_class(class_instance: Class):
    # Get the most recent week_commencing date for each student
    most_recent_assignments = ClassAssignment.objects.filter(
        student=OuterRef('student')
    ).order_by('-week_commencing')

    # Filter ClassAssignment to only those whose most recent assignment is for the given class
    recent_assignments = ClassAssignment.objects.filter(
        student=OuterRef('student'),
        week_commencing=Subquery(most_recent_assignments.values('week_commencing')[:1])
    ).filter(class_name=class_instance)

    # Get the students from the recent_assignments queryset
    students = Student.objects.filter(
        classassignment__in=Subquery(recent_assignments.values('id'))
    ).distinct()

    return students


@component.register("classes_widget")
class ClassesWidget(component.Component):
    template_name = "template.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self):

        # Get distinct class names for the dropdown filter
        class_names = Class.objects.values_list('class_name', flat=True)

        # Construct class assignments dictionary
        class_assignments = {}
        assignments = ClassAssignment.objects.filter(week_until__isnull=True)
        for assignment in assignments:
            class_name = assignment.class_name.class_name
            student_name = assignment.student.student_name
            if class_name not in class_assignments:
                class_assignments[class_name] = []
            class_assignments[class_name].append(student_name)

        return {
            'class_names': class_names
        }

    # class Media:
        # css = "style.css"
        # js = "script.js"



@component.register("student_list")
class StudentList(component.Component):
    template_name = "student_list.html"

    def get(self, request: HttpRequest):
        class_name = request.session.get('class_name')
        class_instance = get_object_or_404(Class, class_name=class_name)
        if class_instance:
            students = get_students_by_class(class_instance)
        else:
            students = None

        context = {'students': students}

        return self.render_to_response(context=context)



