from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Titutlo",
        max_length=40,
        required=True,
        widget = forms.TextInput(attrs={
            'placeholder': "Titulo",
            'class': 'form-control'
        }),
        validators = [
            validators.MinLengthValidator(4, "El título es demasiado corto"),
            validators.RegexValidator('^[a-zA-Z0-9ñ ]*$', 'El título no puede contener caracteres especiales', 'invalid_title')
        ]
    )
    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea,
        validators = [
            validators.MinLengthValidator(10, "El contenido es demasiado corto"),
            validators.MaxLengthValidator(500, "El contenido es demasiado largo"),
        ]
    )
    content.widget.attrs.update({
        'class': 'form-control',
        'rows': 5,
        'placeholder': "Contenido del artículo..."
    })

    public_options = [
        (1, "Si"),
        (0, "No")
    ]
    
    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )
