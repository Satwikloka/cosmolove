from django.core.exceptions import ValidationError


def validate_content(data):
    content = data["content"]
    if content == "":
        raise ValidationError("Content cannot be NULL")
    return data["content"]