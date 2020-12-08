from django.urls import path

from web_framework_softuni.views import index

urlpatterns = [
    path('fram/', index, name='home frame'),
    ]