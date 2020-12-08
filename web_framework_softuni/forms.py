from django import forms

from web_framework_softuni.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'my-textarea',
                },
            ),
            'title': forms.Textarea(
                attrs={'placeholder': 'Time must be greater than zero'}
            )
        }
