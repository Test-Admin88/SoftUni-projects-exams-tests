from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from recipes.views import index, create_recipe, edit_recipe, delete_recipe, details_recipe, like_recipe, dislike_recipe, \
    comment_recipe

urlpatterns = [
    path('', index, name='home page'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete recipe'),
    path('details/<int:pk>', details_recipe, name='details recipe'),
    path('like/<int:pk>', like_recipe, name='like recipe'),
    path('dislike/<int:pk>', dislike_recipe, name='dislike recipe'),
    path('comment/<int:pk>', comment_recipe, name='comment recipe'),
]
