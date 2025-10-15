from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['challenge', 'before_image', 'after_image', 'scale_image', 'location']