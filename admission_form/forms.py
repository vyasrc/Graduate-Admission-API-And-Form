from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator 
from admission import models


class GraduateAdmissionForm(forms.Form):

	gre_score = forms.IntegerField(
		validators=[MinValueValidator(260), MaxValueValidator(340)],
		widget = forms.NumberInput(attrs={'placeholder': 'Enter GRE Score'})
		)
	toefl_score = forms.IntegerField(
		validators=[MinValueValidator(0), MaxValueValidator(120)],
		widget = forms.NumberInput(attrs={'placeholder': 'Enter TOEFL Score'})
		)
	university_rating = forms.FloatField(
		validators=[MinValueValidator(0), MaxValueValidator(5)],
		widget = forms.NumberInput(attrs={'placeholder': 'Enter University Rating(Out of 5)'})
		)
	sop_rating = forms.FloatField(
		validators=[MinValueValidator(0), MaxValueValidator(5)],
		widget = forms.NumberInput(attrs={'placeholder': 'Enter SOP Rating(Out of 5)'})
		)
	lor_rating = forms.FloatField(
		validators=[MinValueValidator(0), MaxValueValidator(5)],
		widget = forms.NumberInput(attrs={'placeholder': 'Enter LOR Rating(Out of 5)'})
		)
	research = forms.ChoiceField(choices = [(0, 0), (1, 1)])
	cgpa = forms.FloatField(
		validators=[MinValueValidator(0), MaxValueValidator(10)],
		widget = forms.NumberInput(attrs={'placeholder': 'Enter CGPA(Out of 10)'})
		)

