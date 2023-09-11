from django import forms
from django.core import validators
def check_for_s(value):
    if value[0].lower()=='s':
        raise forms.ValidationError('name starts with s')

def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('name lenght less than 5')

class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[check_for_s,check_for_len])
    sid=forms.IntegerField()
    sage=forms.IntegerField()
    semail=forms.EmailField(validators=[check_for_s])
    sremail=forms.EmailField(validators=[check_for_s])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    def clean(self):
        e=self.cleaned_data['semail']
        r=self.cleaned_data['sremail']
        if e!=r:
            raise forms.ValidationError('email not match')
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')