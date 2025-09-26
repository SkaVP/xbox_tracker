# from django import forms
# from .models import Game

# class GameForm(forms.ModelForm):
#     class Meta:
#         model = Game
#         fields = ['title', 'genre', 'release_date']
#         widgets = {
#             'release_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'genre': forms.TextInput(attrs={'class': 'form-control'}),
#         }