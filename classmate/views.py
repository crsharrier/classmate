from django.http import HttpRequest, JsonResponse
from django.forms import BaseForm, ModelForm
from django.template.response import TemplateResponse
from django.apps import apps

from classmate.models import Class, Student, Job, TermPeriod
from classmate.forms import forms_dict

def home_view(request: HttpRequest):
    context = {}
    return TemplateResponse(request, 'index.html', context)

def seating_view(request: HttpRequest):
    desks = [
        {'position': [50, 50], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [250, 50], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [450, 50], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [650, 50], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [50, 200], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [250, 200], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [450, 200], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [650, 200], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [50, 350], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [250, 350], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [450, 350], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
        {'position': [650, 350], 'rotation': 0, 'student_1': 'student 1', 'student_2': 'student 2'},
    ]
    context = {'desks': desks}
    return TemplateResponse(request, 'seating.html', context)

def jobs_view(request: HttpRequest):
    context = {}
    return TemplateResponse(request, 'jobs.html', context)

def lining_up_view(request: HttpRequest):
    context = {}
    return TemplateResponse(request, 'lining_up.html', context)

def lists_view(request: HttpRequest):      
    context = {
        'classes': [{'pk': cl.id, 'name': cl.class_name} for cl in Class.objects.all()],
        'students': [{'pk': st.id, 'name': st.student_name} for st in Student.objects.all()],
        'jobs': [{'pk': jb.id, 'name': jb.job_name} for jb in Job.objects.all()],
        'term_periods': [{'pk': tp.week_commencing, 'name': tp.period_name} for tp in TermPeriod.objects.all()]
    }
    return TemplateResponse(request, 'lists.html', context)

def settings_view(request: HttpRequest):
    context = {}
    return TemplateResponse(request, 'settings.html', context)


# ==============================================================================
# CRUD Dialogs:
# ==============================================================================
def crud_dialog(request: HttpRequest):
    if request.method == 'POST':
        entity = request.GET.get('entity')
        action = request.GET.get('action')

        form = forms_dict.get(entity)
        filled_form: ModelForm = form(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return JsonResponse({'message': 'Entity successfully saved'})
            
    
    elif request.method == 'DELETE':

        return JsonResponse({'message': 'Entity successfully deleted'})
            

    elif request.method == 'GET':
        action = request.GET.get('action')
        entity = request.GET.get('entity')
        pk = request.GET.get('pk')
        form = forms_dict.get(entity)

        # edit request: 
        if pk:
            model = apps.get_model('classmate', entity)
            instance = model.objects.get(pk=pk)
            form = form(instance=instance)

        context = {
            'action': action, 
            'entity': entity,
            'form': form
            }
        return TemplateResponse(request, 'partials/crud_dialog.html', context)

