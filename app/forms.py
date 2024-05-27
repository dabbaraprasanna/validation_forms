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
     u=forms.URLField()
     em=forms.EmailField()
     reemail=forms.EmailField()
     bootcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
     def clean(self):
        e=self.cleaned_data['em']
        re=self.cleaned_data['reemail']
        if e!=re:
            raise forms.ValidationError('both are not mathing')
     def clean_bootcatcher(self):
        cu=self.cleaned_data['bootcatcher']
        if  len(cu)>0:
            raise forms.ValidationError('it should be none')
    


