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
    context = {}
    return TemplateResponse(request, 'seating.html', context)

def jobs_view(request: HttpRequest):
    context = {}
    return TemplateResponse(request, 'jobs.html', context)

def lining_up_view(request: HttpRequest):
    context = {}
    return TemplateResponse(request, 'lining_up.html', context)

def lists_view(request: HttpRequest):      
    context = {
        'classes': [cl.class_name for cl in Class.objects.all()],
        'students': [st.student_name for st in Student.objects.all()],
        'jobs': [jb.job_name for jb in Job.objects.all()],
        'term_periods': [tp for tp in TermPeriod.objects.all()]
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

