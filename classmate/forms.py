from django.forms import ModelForm
from classmate.models import Student, Class, Job, TermPeriod

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class TermPeriodForm(ModelForm):
    class Meta:
        model = TermPeriod
        fields = '__all__'

forms_dict = {
    'class': ClassForm,
    'job': JobForm,
    'student': StudentForm,
    'term period': TermPeriodForm
}
