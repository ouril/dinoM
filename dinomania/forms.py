from django import forms
from .models import New, Dino, Book, Autor, Resurs

class NewsForm(forms.ModelForm):
    class Meta:
       model = New
       fields = ('__all__')

class DinoForm(forms.ModelForm):
    class Meta:
        model = Dino
        fields = ('__all__')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('__all__')

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('__all__')


class ResursForm():
    class Meta:
        model = Resurs
        fields = ('__all__')