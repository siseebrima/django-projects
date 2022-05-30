
from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'stars']
            

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(max_length=50, label='First Name')
#     last_name = forms.CharField(max_length=50, label='Last Name')
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Enter your review', widget=forms.widgets.Textarea())