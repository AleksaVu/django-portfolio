from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nickname',
                  'comment'
                  ]
        # fields = '__all__'


# class CommentForm(forms.ModelForm):
#     nickname = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Pick nickname', 'label': 'Nickname:'}))
#     comment = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Comment here', 'label': 'Comment:'}))


# class CommentForm(forms.Form):
#     nickname= forms.CharField(max_length=100)
#     nickname.widget.attrs.update({'class': 'form-label'})
#     comment = forms.CharField(max_length=100)
#     comment.widget.attrs.update(size='100')
