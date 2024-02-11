from rest_framework import serializers
from .models import GlobalInformation, AboutMe, Experience, ExperienceDetail, Formation

class GlobalInformationSerializer(serializers.ModelSerializer):

	class Meta:
		model = GlobalInformation
		fields = ('last_name','first_name','job_title','mail','linkedin','github','codingame','languages')

class AboutMeSerializer(serializers.ModelSerializer):

	class Meta:
		model = AboutMe
		fields = ('description_text','extra_profesionnal_sports','extra_profesionnal_activity')

class ExperienceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Experience
		fields = ('type_experience','programming_languages','tools_used','description','starting_date','ending_date','job_title','company','city')

class ExperienceDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = ExperienceDetail
		fields = ('goal','detail','accomplishment')

class FormationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Formation
		fields = ('starting_date','ending_date','title','accomplishment')