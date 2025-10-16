from django import forms

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Titutlo",
        max_length=40,
        required=True,
        widget = forms.TextInput(attrs={
            'placeholder': "Titulo",
            'class': 'form-control'
        })
    )
    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea
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
