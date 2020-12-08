from django.db import models
from recipes.validators import validate_time_greater_bigger


class Recipe(models.Model):
    title = models.CharField(max_length=30, blank=False)
    # image_url = models.URLField("Image URL", blank=False)
    description = models.TextField(blank=False,)
    ingredients = models.CharField(max_length=250, blank=False)
    time = models.IntegerField(
        'Time(Minutes)',
        validators=(validate_time_greater_bigger,),
    )
    recipe_image = models.ImageField(blank=False, upload_to='recipe_images')

    def __str__(self):
        return f'{self.title}'


class Likes(models.Model):
    for_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # test = models.CharField(max_length=2)


class Dislike(models.Model):
    which_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField(blank=False)