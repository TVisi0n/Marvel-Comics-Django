from django.forms import ModelForm
from .models import Comic

class ComicForm(ModelForm):
    class Meta:
        model = Comic
        fields = '__all__'
