from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.utils import timezone

from .models import GlobalInformation, AboutMe

# Create your views here.
def index(request, language="FR"):
	template_name = "front_page/index.html"
	context_object_name = "global_information"
	language = language.upper()

	informations = get_object_or_404(GlobalInformation, pk=language)

	try:
		has_about_me = AboutMe.objects.get(pk=1)
	except AboutMe.DoesNotExist:
		raise Http404("The section 'About me' is missing")

	return render(request, template_name, {context_object_name: informations})
