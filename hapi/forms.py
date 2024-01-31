from django import forms


class SearchForm(forms.Form):
    user_search = forms.CharField(label="Your Search", max_length=100)
    orientation = forms.CharField(
        label="Orientation",
        max_length=20,
        required=False,
        help_text="Valid values are: landscape, portrait, squarish"
    )
    color = forms.CharField(
        label="Color",
        max_length=20,
        required=False,
    )
