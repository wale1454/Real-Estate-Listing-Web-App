from attr import fields
from django import forms

from django.forms import ModelForm
from estateapp.models import Property


class createProperty(ModelForm):

    class Meta:

        model = Property
        fields = "__all__"
