from django.core.exceptions import ValidationError

def validate_digits(value):
    if not value.isdigit():
        raise ValidationError(
            '%(value)s is not a valid national ID. It must contain only digits.',
            params={'value': value},
        )

def validate_national_id(value):
    if len(value) != 12:
        raise ValidationError(
            '%(value)s is not a valid national ID. It must be exactly 12 digits long.',
            params={'value': value},
        )
    
    if not value.isdigit():
        raise ValidationError(
            '%(value)s is not a valid national ID. It must contain only digits.',
            params={'value': value},
        )
