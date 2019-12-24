from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
class GraduateAdmission(models.Model):
	RESEARCH_CHOICES = ((0, 0), (1, 1))

	gre_score = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(260), MaxValueValidator(340)])
	toefl_score = models.PositiveIntegerField(default = 0, validators=[MaxValueValidator(120)])
	university_rating = models.FloatField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	sop_rating = models.FloatField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	lor_rating = models.FloatField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	research = models.PositiveIntegerField(default = 0, choices = RESEARCH_CHOICES)
	cgpa = models.FloatField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(10)])

	def __str__(self):
		return self.cgpa


