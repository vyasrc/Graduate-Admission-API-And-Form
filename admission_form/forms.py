from django import forms
from . import models


class GraduateAdmissionForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(GraduateAdmissionForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['placeholder'] = 'Enter Name'
		self.fields['gre_score'].widget.attrs['placeholder'] = 'Enter GRE Score'
		self.fields['toefl_score'].widget.attrs['placeholder'] = 'Enter TOEFL Score'
		self.fields['university_rating'].widget.attrs['placeholder'] = 'Enter University Rating(Out of 5)'
		self.fields['sop_rating'].widget.attrs['placeholder'] = 'Enter SOP Rating(Out of 5)'
		self.fields['lor_rating'].widget.attrs['placeholder'] = 'Enter LOR Rating(Out of 5)'
		self.fields['cgpa'].widget.attrs['placeholder'] = 'Enter CGPA(Out of 10)'

	class Meta:
		model = models.GraduateAdmission
		fields = '__all__' 

