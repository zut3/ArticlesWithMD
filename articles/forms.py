from django import forms
from . import models


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-controll input", "required": True,
                                            "placeholder": "Title",
                                            "label": ""}), label='')

    text = forms.CharField(widget=forms.Textarea(attrs={"class": "textarea",
                                                        "id": "md-text",
                                                        "placeholder": "Text of article",
                                                        "label": "",
                                                        }), label='', initial="# Hello world!  ")

    class Meta:
        model = models.Article
        fields = ["title", "text"]
