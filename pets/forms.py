from django import forms
from .models import Pets
from . import constant


class PetForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields: list[str] = ["name", "species", "year_of_birth"]

    widgets: dict[str, forms.ChoiceField] = {
        "species": forms.ChoiceField(label="Species", choices=constant.OPTIONS_SPECIES, required=True),
        "year_of_birth": forms.ChoiceField(label="Year of Birth", choices=constant.OPTIONS_YEARS, required=True),
    }
    