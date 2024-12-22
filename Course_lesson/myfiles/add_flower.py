from django import forms
from .models import Course
class Gullarforms(forms.Form):
    title = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "placeholder":"Nomini kiriting",
        "class":"form-control"
    }),label="Nomi")
    content = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder":"Matnini kiriting",
        "class":"form-control"
    }),required=False)
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        "class":"form-control"
    }),required=False)
    category = forms.ModelChoiceField(queryset=Course.objects.all(),widget=forms.Select(attrs={
        "class":"form-select"
    }))
    published = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        "class":"form-check-input",
        "checked":"checked"
    }))