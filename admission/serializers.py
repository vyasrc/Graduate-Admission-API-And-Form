from rest_framework import serializers
from admission import models


class GraduateAdmissionSerializer(serializers.ModelSerializer):


	class Meta:
		model = models.GraduateAdmission
		fields = '__all__'
