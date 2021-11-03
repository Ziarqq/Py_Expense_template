from prompt_toolkit.validation import Validator, ValidationError
from PyInquirer import prompt
from six import string_types

class NumberValidator(Validator):
    def validate(self, document):
        is_ok = True

        try:
            int_n = int(document.text)
        except ValueError:
            is_ok = False
        
        try:
            float_n = float(document.text)
        except ValueError:
            is_ok = False
        
        if not is_ok:
            raise ValidationError(
                message='Please enter a valid number',
                cursor_position=len(document.text))

class StringValidator(Validator):
    def validate(self, document):
        string_to_check = document.text

        if not string_to_check.isalpha():
            raise ValidationError(
                message='Please enter a valid label',
                cursor_position=len(document.text))