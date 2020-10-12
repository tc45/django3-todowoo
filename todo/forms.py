from django.forms import ModelForm
from .models import Todo
# Create new forms here

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
