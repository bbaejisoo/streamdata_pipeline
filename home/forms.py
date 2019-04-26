from django import forms
from .models import Grafana
from django.contrib.admin.widgets import AdminSplitDateTime


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
                'required': True,
                'placeholder': 'http://<grafana server>:3000/...'
            }),
            'start_time': AdminSplitDateTime(attrs={
                'id': 'start_time',
                'required': True
            }),
            'end_time': AdminSplitDateTime(attrs={
                'id': 'end_time',
                'required': True
            }),
        }