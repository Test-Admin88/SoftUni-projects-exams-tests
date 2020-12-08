from django.core.exceptions import ValidationError


def validate_time_greater_bigger(value):
    if value <= 0:
        raise ValidationError('Please insert a positive value. Time cannot be negative or zero.')
