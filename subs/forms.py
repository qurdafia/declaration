from django import forms
from .models import Sub


class SubForm(forms.ModelForm):

    class Meta:
        model = Sub
        fields = ('name', 'mobile_number', 'company', 'visit_pass_number', 'purpose', 'temperature', 'time_scanned', 'is_quarantined', 'is_contacted', 'has_travelled', 'is_unwell', 'reg_date', 'acknowledge')
