from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year_from_1900_to_current(value):
    if value < 1900 or value > datetime.now().year:
        raise ValidationError(f"{value} is not a correct year!")

def validate_image_less_than_5mb(image):
    filesize = image.file.size
    megabyte_limit = 5
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f'Max file size is {megabyte_limit}MB')