from django import template

register = template.Library()


@register.inclusion_tag('frameworks/tags/bootstrap_form.html')
def bootstrap_form(form, action, method):

    for (_, field) in form.fields.items():
        if 'class' not in field.widget.attrs: # if you do not have one, make it - '' and then ... this is because of the widget my text area
            field.widget.attrs['class'] = '' # iterate through the form fileds and attach classes to them /our form creates/attaches classes css ?

        field.widget.attrs['class'] += 'form-control'
    return {'form': form,
            'action': action,
            'method': method
            }
