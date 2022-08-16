from django import forms

from .models import MixSItemSpecs, MixSCheckResult, MixSCheckDetail


class MixSForm(forms.ModelForm):
    class Meta:
        model = MixSCheckDetail
        fields = ['check_result', 'batch', 'mv']
