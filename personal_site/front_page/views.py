from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.utils import timezone

from .models import GlobalInformation, AboutMe

# Create your views here.
class IndexView(generic.DetailView):
	template_name = "front_page/index.html"
	context_object_name = "global_information"

	def get_queryset(self):
		return GlobalInformation.objects.order_by("languages")