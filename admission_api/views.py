from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from admission_form.models import GraduateAdmission
from . serializers import GraduateAdmissionSerializer
from sklearn.externals import joblib
import numpy as np
import os 


class GraduateAdmissionView(viewsets.ModelViewSet):
	queryset = GraduateAdmission.objects.all()
	serializer_class = GraduateAdmissionSerializer
	http_method_names = ['get', 'head']

		
@api_view(["POST"])
def admission_chance(request):
	try:
		path = os.getcwd()
		model=joblib.load(path + '/admission_model.pkl')
		data=request.data
		unit=np.array(list(data.values()))
		unit=unit.reshape(1,-1)
		y_pred=model.predict(unit)
		print(y_pred)
		score = round(y_pred[0][0]* 100, 2)
		return JsonResponse('Your chance of admission is {}%'.format(score), safe=False)
	except:
	 	return Response(status.HTTP_400_BAD_REQUEST)



