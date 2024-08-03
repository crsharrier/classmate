from django_components import component
from django.db import models
from classmate.models import TermPeriod

@component.register("term_period_widget")
class TermPeriodWidget(component.Component):
    template_name = "template.html"

    def get_context_data(self, index: int):
        term_periods = TermPeriod.objects.all()
        return {
            'term_periods': term_periods,
            'index': index
        }

    # class Media:
    #     js = 'script.js'