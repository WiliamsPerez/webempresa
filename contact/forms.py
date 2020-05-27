from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Escribe tu Nombre.'}
    ),min_length=5, max_length=20)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder': 'Escribe tu email.'}
    ),min_length=20, max_length=30)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 4, 'placeholder': 'Escribe tu mensaje.'}
    ),min_length=20, max_length=200)