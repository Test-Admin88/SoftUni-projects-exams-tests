from django.shortcuts import render

from web_framework_softuni.forms import TodoForm
from web_framework_softuni.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
        'state': True, # this is how u use the filter from templatetags and context, after u give it here, u have to change it in the template index as well
        'forms': TodoForm,  # 13
    }
    return render(request, 'frameworks/index.html', context)
