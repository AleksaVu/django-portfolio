from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nickname',
                  'comment'
                  ]
        # fields = '__all__'
        widgets = {
            'nickname' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter nickname'}),
            'comment' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter comment', 'label': 'Body'})            
        }    



