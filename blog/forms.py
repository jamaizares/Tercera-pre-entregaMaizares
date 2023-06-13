
from django import forms

from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class serviciosForm(forms.ModelForm):

        class Meta:
             model = servicios
             fields = ('nombre', 'tipo','precio')
