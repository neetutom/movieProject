from django import forms
from .models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['movie_name', 'movie_desc', 'movie_year', 'movie_img']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['movie_name'].widget.attrs.update({'class':'form-control'})
        self.fields['movie_desc'].widget.attrs.update({'class': 'form-control'})
        self.fields['movie_year'].widget.attrs.update({'class': 'form-control'})
        self.fields['movie_img'].widget.attrs.update({'class': 'form-control'})





