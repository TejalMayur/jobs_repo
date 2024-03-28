from django import forms

class Studentform(forms.Form):
    name=forms.CharField(max_length=20)
    marks=forms.IntegerField()
    age=forms.IntegerField()
