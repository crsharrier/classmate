from django.http import HttpRequest, JsonResponse
from django.forms import BaseForm, ModelForm
from django.template.response import TemplateResponse
from django.apps import apps

from classmate.models import Class, SeatingLayout, Student, Job, TermPeriod, models_dict
from classmate.forms import forms_dict

from datetime import datetime

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
    term_periods = [
        {'pk': tp.week_commencing.strftime('%Y-%m-%d'), 'info': (tp.week_name, tp.period_name)} 
        for tp in TermPeriod.objects.all()
        ]
    classes = [
        {'pk': cl.id, 'info': (cl.class_name,)}
        for cl in Class.objects.all()
    ]
    context = {'desks': desks,
               'classes': classes,
               'term_periods': term_periods}
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

# ==============================================================================
# seating canvas:
# ==============================================================================
def seating_layout(request: HttpRequest):
    print('request.GET:', request.GET)
    entity = request.GET.get('entity')
    pk = request.GET.get('pk')

    if entity == 'period':
        request.session['st_period_pk'] = pk
    elif entity == 'class':
        request.session['st_class_pk'] = pk
        class_obj = Class.objects.get(id=pk)
        request.session['st_class_name'] = class_obj.class_name

    class_pk = request.session.get('st_class_pk'),
    class_name = request.session.get('st_class_name'),
    class_name = class_name[0] if class_name else None

    period_pk = request.session.get('st_period_pk')
    class_obj = Class.objects.filter(id=class_pk[0]).first()

    period_obj = TermPeriod.objects.filter(week_commencing=period_pk).first()
    period_name = period_obj.period_name if period_obj else None

    seating_layout = SeatingLayout.objects.filter(class_id=class_obj, period=period_obj).first()

    context = {
        'class_pk': class_pk,
        'class_name': class_name,
        'period_pk': period_pk,
        'period_name': period_name,
        'seating_layout': seating_layout
    }
    return TemplateResponse(request, 'partials/seating_layout.html', context)
    