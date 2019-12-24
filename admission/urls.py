from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('admission', views.GraduateAdmissionView) 

urlpatterns = [
    path('api/', include(router.urls)),
    path('status/', views.admission_chance)
]
