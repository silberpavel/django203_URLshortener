from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
    url_validator = URLValidator()
    value_1_invalid = False
    value_2_invalid = False
    try:
        url_validator(value)
    except:
        value_1_invalid = True

    value_2_url = "http://" + value
    try:
        url_validator(value_2_url)
    except:
        value_2_invalid = True
    value_2_url = "http://" + value
    if value_1_invalid == False and not value_2_invalid == False:
        raise ValidationError("Invalid URL for this field")
    return value


def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("This is not valid becausee no .com")
    return value



