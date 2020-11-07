from django.shortcuts import render, redirect


from recipes.forms.recipeforms import DeleteRecipeForm, RecipeForm
from recipes.models import Recipe


def index(request):
    # if Recipe.objects.exists():
    recipes = Recipe.objects.all()
    context = {
            'recipes': recipes
            }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        context = {
            'form': RecipeForm()
        }
        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {
            'form': form,
        }

        return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        context = {
            'recipe': recipe,
            'form': form,
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        context = {
            'recipe': recipe,
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('home page')
        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': DeleteRecipeForm(instance=recipe)
        }
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('home page')


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    strings_maybe = getattr(recipe, 'ingredients')
    with_comma = strings_maybe.replace(' ', ', ')
    with_comma += ','
    word_list = []
    word = ''
    for el in with_comma:
        if el == ',':
            word_list.append(word)
            word = ''
            continue
        word += el
    context = {
        'ingredients_list': word_list,
        'obj_recipe': recipe,
    }
    return render(request, 'details.html', context)

