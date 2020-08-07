from django import forms
from .models import Image

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['name', 'picture']

class InstaForm(forms.Form):
    Hashtag = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[a-z]+', 'title':'Enter only lowercase ltters '}))
    Image_numbers= forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off', 'placeholder':'500 Max','type': 'number', 'max':'500','pattern':'[0-9]+', 'title':'Enter only numbers'}))
    