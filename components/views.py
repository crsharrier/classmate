from django.http import HttpRequest, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class SelectedClassView(View):

    def get(self, request: HttpRequest, *args, **kwargs):
        selected_class = request.session.get('selected_class', None)
        return JsonResponse({'selected_class': selected_class})

    def post(self, request: HttpRequest, *args, **kwargs):
        class_name = request.POST.get('class_name')
        if class_name:
            request.session['selected_class'] = class_name
            return JsonResponse({'status': 'success', 'selected_class': class_name})
        else:
            return JsonResponse({'status': 'error', 'message': 'Class name not provided'}, status=400)
