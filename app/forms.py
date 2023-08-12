from django import forms

def validate_for_a(svalue):
    if svalue[0]=='a':
        raise forms.ValidationError('it is a validation')


class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_for_a])
    sage=forms.IntegerField()