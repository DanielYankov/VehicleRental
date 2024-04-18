from django.core import exceptions
def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed')

def validate_all_capital(value):
    if value != value.upper():
        raise exceptions.ValidationError("Only capital letters are allowed.")