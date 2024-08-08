from django_components import component
from django.db import models

@component.register("accordion_slot")
class AccordionSlot(component.Component):
    template_name = "template.html"

    def get_context_data(self, 
                         index: int, 
                         title: str,
                         entity: str,
                         iterable: list,
                         always_open = False,
                         nested_accordion = None,
                         ):
        return {
            'index': index,
            'title': title,
            'entity': entity,
            'iterable': iterable,
            'always_open': always_open,
            'nested_accordion': nested_accordion
        }

    class Media:
        js = 'script.js'