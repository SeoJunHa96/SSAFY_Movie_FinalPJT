from django import forms
from .models import Movie, Comment


# class MovieForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'content',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)