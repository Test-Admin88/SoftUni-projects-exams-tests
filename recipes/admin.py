from django.contrib import admin

from recipes.models import Recipe, Likes, Comment

admin.site.register(Recipe)
admin.site.register(Likes)
admin.site.register(Comment)