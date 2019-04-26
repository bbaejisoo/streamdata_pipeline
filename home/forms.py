from django import forms
from .models import Grafana
#from django.contrib.admin.widgets import AdminSplitDateTime
from bootstrap_datepicker_plus import DateTimePickerInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Grafana
        fields = ['embed_url', 'start_time', 'end_time']

        labels = {
            'embed_url': 'Grafana_Embed URL',
        }

        widgets = {
            'embed_url': forms.TextInput(attrs={
                'id': "embed_url",
                'class': "form-control",
                'required': True,
                'placeholder': 'http://<grafana server>:3000/...'
            }),
            'start_time': DateTimePickerInput(attrs={
                'id': 'start_time',
                'class': "form-control",
                'required': True
            }, format="%Y-%m-%d %H:%M"),
            'end_time': DateTimePickerInput(attrs={
                'id': 'end_time',
                'class': "form-control",
                'required': True
            }, format="%Y-%m-%d %H:%M"),
        }