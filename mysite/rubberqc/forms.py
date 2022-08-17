from django import forms

from .models import MixSItemSpecs, MixSCheckResult, MixSCheckDetail


class MixSForm(forms.ModelForm):
    class Meta:
        model = MixSCheckDetail
        fields = '__all__'

