from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(max_length=20, required=True)
    Email = forms.EmailField(max_length=50, required=True)
    subject = forms.CharField(max_length=50, required=True)
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea()
    )
