from django_components import component
from django.apps import apps

@component.register("list_item")
class ListItem(component.Component):
    template_name = "template.html"

    def get_context_data(self, pk: str, entity: str, can_edit: bool=True):        
        return {
            'pk': pk,
            'entity': entity,
            'can_edit': can_edit
        }

    class Media:
        js = 'script.js'
