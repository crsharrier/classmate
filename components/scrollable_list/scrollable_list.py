from django_components import component
from django.db import models

@component.register("scrollable_list")
class ScrollableList(component.Component):
    template_name = "template.html"

    def get_context_data(self, 
                         index: int, 
                         title: str,
                         entity: str,
                         iterable: list,
                         hx_get: str,
                         hx_target: str,
                         can_add = False
                         ):

        return {
            'index': index,
            'title': title,
            'entity': entity,
            'iterable': iterable,
            'hx_get': hx_get,
            'hx_target': hx_target,
            'can_add': can_add
        }

    class Media:
        js = 'script.js'