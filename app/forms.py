from django import forms

from app.models import *

def validate_is_b(value):
    if value[0]=='b':
        raise forms.ValidationError('should not start with b')

def validate_is_len(value):
    if len(value)<5:
        raise forms.ValidationError('should be more than  5')

class TopicForm(forms.Form):
    topic_name=forms.CharField(validators=[validate_is_b,validate_is_len])

class WebpageForm(forms.Form):
     tn=forms.ModelChoiceField(queryset=Topic.objects.all())
     na=forms.CharField(validators=[validate_is_b,validate_is_len])
     em=forms.EmailField()
     u=forms.URLField()

