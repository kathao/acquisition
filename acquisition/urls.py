from django.contrib import adim
from django.urls import path

from acquisition import views

urlpatterns = [
	path('upload/', views.upload, name ='upload'),
	path('adim/', admin.site.urls),
]