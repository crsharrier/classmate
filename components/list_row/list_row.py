from django_components import component
from django.apps import apps

@component.register("list_row")
class ListRow(component.Component):
    template_name = "template.html"

    def get_context_data(self, 
                         pk: str, 
                         info: tuple, 
                         entity: str,
                         hx_get: str,
                         hx_target: str,
                         can_edit: bool=True):        
        return {
            'pk': pk,
            'info': info,
            'entity': entity,
            'hx_get': hx_get,
            'hx_target': hx_target,
            'can_edit': can_edit
        }

    class Media:
        js = 'script.js'
