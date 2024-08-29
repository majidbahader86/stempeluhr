from django import forms
from .models import TimeEntry

class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ['start_time', 'end_time', 'description']
