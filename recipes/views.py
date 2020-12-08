from django.shortcuts import render, redirect


from recipes.forms.recipeforms import DeleteRecipeForm, RecipeForm, CommentForm
from recipes.models import Recipe, Likes, Dislike, Comment


def index(request):
    # if Recipe.objects.exists():
    recipes = Recipe.objects.all()
    context = {
            'recipes': recipes
            }
    sda = 0
    return render(request, 'recipes/index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        context = {
            'form': RecipeForm()
        }
        return render(request, 'recipes/create.html', context)
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {
            'form': form,
        }

        return render(request, 'recipes/create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        context = {
            'recipe': recipe,
            'form': form,
        }
        return render(request, 'recipes/edit.html', context)
    else:
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        context = {
            'recipe': recipe,
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('home page')
        return render(request, 'recipes/edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': DeleteRecipeForm(instance=recipe)
        }
        return render(request, 'recipes/delete.html', context)
    else:
        recipe.delete()
        return redirect('home page')


def separate_ingredients(recipe, ):
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
    return word_list


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    separated_ingredients = separate_ingredients(recipe)
    form = CommentForm()
    context = {
        'ingredients_list': separated_ingredients,
        'obj_recipe': recipe,
        'comment_form': form,
    }
    return render(request, 'recipes/details.html', context)


def like_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    like = Likes(for_recipe=recipe)
    like.save()
    return redirect('details recipe', pk)


def dislike_recipe(request, pk):
    # recipe = Recipe.objects.get(pk=pk)
    like = Dislike(which_recipe_id=pk)
    like.save()
    return redirect('details recipe', pk)


def comment_recipe(request, pk):
    if request.method == 'GET':
        return render(request, 'recipes/details.html', pk)
    else:
        recipe = Recipe.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.recipe = recipe
            comment.save()
            return redirect('details recipe', pk)
        separated_ingredients = separate_ingredients(recipe)
        context = {
            'ingredients_list': separated_ingredients,
            'obj_recipe': recipe,
            'comment_form': form,
        }
        return render(request, 'recipes/details.html', context)
