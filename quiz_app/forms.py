
from tabnanny import verbose
from django import forms

from quiz_app.models import Question, Variant, Quiz

class VarForm(forms.ModelForm):
    text = forms.CharField(disabled=True, label='')
    checked = forms.BooleanField(required=False, label='')
    id = forms.IntegerField()
    class Meta:
        model = Variant
        fields = ['text', 'checked', 'id']

FormFactory = forms.inlineformset_factory(Question, Variant, 
                                          extra=0, form=VarForm, can_delete=False)