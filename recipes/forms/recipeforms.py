from django import forms

from recipes.forms.common import DisabledFormMixin
from recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    recipe_image = forms.ImageField(widget=forms.FileInput, )

    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'This is the title'}),
        }


class DeleteRecipeForm(RecipeForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
