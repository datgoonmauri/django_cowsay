from django import forms
from pysay.models import Cowsay

class Cow_Form(forms.ModelForm):

	class Meta:
		model = Cowsay
		fields = ['text']