from django import forms
from .models import SharedFile

class FileUploadForm(forms.ModelForm):
    expiry = forms.IntegerField(
        required=False,
        label='Expiry (in hours)',
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 24'})
    )
    class Meta:
        model = SharedFile
        fields = ['file', 'password', 'expiry']
