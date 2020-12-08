# Generated by Django 3.1.2 on 2020-11-08 14:15

from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(validators=[recipes.validators.validate_time_greater_bigger], verbose_name='Time(Minutes)'),
        ),
    ]