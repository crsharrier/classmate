from django.http import HttpRequest, JsonResponse
from classmate.models import Student, Class, Job

def add_student(request: HttpRequest):
    new_student_name = request.GET.get('new_student_name')
    new_student = Student(student_name=new_student_name)
    new_student.save()
    return JsonResponse({'message': f'New student {new_student_name} added successfully'})

def delete_student(request: HttpRequest, student_name):
    try:
        student = Student.objects.get(student_name=student_name)
        student.delete()
        return JsonResponse({'message': f'Student {student_name} deleted successfully'}, status=204)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    