from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"class": "form-control feedback", "placeholder": "Уи цӏэр"}
        ),
        required=False,
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control feedback", "placeholder": "Уи email-р"}
        ),
        required=False,
    )
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={"class": "form-control feedback", "placeholder": "Тхыгъэр"}
        ),
        required=False,
    )
