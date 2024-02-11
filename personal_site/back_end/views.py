from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import GlobalInformation, AboutMe, Experience, ExperienceDetail, Formation
from .serializers import *

def index(request):
	return HttpResponseRedirect(reverse("back_end:informations", args=("fr",)))

@api_view(['GET'])
def global_information(request, language):
	language = language.upper()

	data = get_object_or_404(GlobalInformation, pk=language)
	serializer = GlobalInformationSerializer(data, context={'request': request})

	return Response(serializer.data)

@api_view(['GET'])
def about(request, language):
	language = language.upper()

	data = get_object_or_404(AboutMe, language=language)
	serializer = AboutMeSerializer(data, context={'request': request})

	return Response(serializer.data)

@api_view(['GET'])
def experiences(request, language):
	language = language.upper()

	data = Experience.objects.all().filter(language=language)
	serializer = ExperienceSerializer(data, context={'request': request}, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def formations(request, language):
	language = language.upper()

	data = Formation.objects.all().filter(language=language)
	serializer = FormationSerializer(data, context={'request': request}, many=True)

	return Response(serializer.data)
