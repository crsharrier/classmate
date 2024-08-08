from django_components import component
from django.apps import apps

@component.register("list_item")
class ListItem(component.Component):
    template_name = "template.html"

    def get_context_data(self, item_dict: dict, entity: str, can_edit: bool=True):        
        return {
            'pk': item_dict['pk'],
            'name': item_dict['name'],
            'entity': entity,
            'can_edit': can_edit
        }

    class Media:
        js = 'script.js'
