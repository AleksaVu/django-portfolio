from django import forms
from .models import Project


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name',
                  'description',
                  'completed',
                  'language',
                  'link',
                  'member',
                  ]
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Project Name'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'language' : forms.Select(attrs={'class': 'form-select', 'placeholder': 'Language'}),
            'link' : forms.URLInput(attrs={'class': 'form-control', 'labe': 'Link:'}),
            'member' : forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'Enter nickname'}),            
        }    
