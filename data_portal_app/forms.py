# Inside data_portal_app/forms.py

from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
