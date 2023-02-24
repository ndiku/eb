import datetime
from django.core.exceptions import ValidationError
from django.db import models
from . import constant


class Pets(models.Model):
    """
    Pets Model.

    Args:
        models.Model : object

    Raises:
        ValidationError: validation error
        ValidationError: Validation error

    Returns:
        obj: Pet object
    """

    id: int = models.IntegerField(primary_key=True, editable=False)

    name: str = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Name",
    )

    species: str = models.CharField(
        max_length=10,
        choices=constant.OPTIONS_SPECIES,
        blank=False,
        verbose_name="Species",
    )

    year_of_birth: int = models.IntegerField(
        choices=constant.OPTIONS_YEARS,
        default=datetime.datetime.now().year,
        blank=False,
        verbose_name="Year of Birth",
    )

    def clean(self):
        """
        Clean method.

        Raises:
            ValidationError: _description_
            ValidationError: _description_
        """
        if self.year_of_birth <= 1950:
            raise ValidationError("Year of birth must be greater than 1950")
        if self.year_of_birth > datetime.datetime.now().year:
            raise ValidationError("Year of birth cannot be in the future")

    def __str__(self) -> str:
        return self.name

    def fetch(self, id) -> object:
        return Pets.objects.get(pk=id)
