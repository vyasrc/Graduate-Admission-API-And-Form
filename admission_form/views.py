from . forms import GraduateAdmissionForm
from rest_framework.response import Response
from sklearn.externals import joblib
import numpy as np
import os 
from django.shortcuts import render
from django.contrib import messages
		

def admission_score(data):
	try:
		path = os.getcwd()
		model=joblib.load(path + '/admission_model.pkl')
		if 'csrfmiddlewaretoken' in data:
			del data['csrfmiddlewaretoken']
		unit=np.array(list(data.values()))
		unit=unit.reshape(1,-1)
		y_pred=model.predict(unit)
		score = round(y_pred[0][0]* 100, 2)
		return score
	except:
	 	return Response(status.HTTP_400_BAD_REQUEST)

def admission_chance_form(request):
	if request.method == 'POST':
		form = GraduateAdmissionForm(request.POST)
		if form.is_valid():
			gre_score = form.cleaned_data['gre_score']
			toefl_score = form.cleaned_data['toefl_score']
			university_rating = form.cleaned_data['university_rating']
			sop_rating = form.cleaned_data['sop_rating']
			lor_rating = form.cleaned_data['lor_rating']
			research = form.cleaned_data['research']
			cgpa = form.cleaned_data['cgpa']
			data = (request.POST).dict()
			score = admission_score(data)
			messages.success(request, 'Your chance of admission is {}%'.format(score))

	form = GraduateAdmissionForm()

	return render(request, 'form/form.html', {'form': form})



