from django import template

from web_framework_softuni.models import Todo

register = template.Library()


@register.inclusion_tag('frameworks/tags/todo-item.html')
def todo_details(todo):
    return {'todo':todo,
            'todos_count': Todo.objects.count()}  # when u call todo_details tag - render the f.workds/tags ... template and give it as context todo dict
    # return f'<h1>{todo.text}</h1>' #10