from django.db import models
from django.utils import timezone
from django.contrib import admin

class GlobalInformation(models.Model):
	LANGUAGES = {
		"FR": "FR",
		"EN": "EN",
	}
	last_name = models.CharField(max_length=20)
	first_name = models.CharField(max_length=20)
	job_title = models.CharField(max_length=20)
	mail = models.EmailField()
	linkedin = models.URLField(max_length=200)
	github = models.URLField(max_length=200)
	codingame = models.URLField(max_length=200)
	languages = models.CharField(max_length=2, choices=LANGUAGES, primary_key=True)

	def __str__(self):
		return f"Global information for language {self.languages}"

class Experience(models.Model):
	TYPE_EXPERIENCES = {
		"perso": "Personal",
		"pro": "Professional",
	}
	language = models.ForeignKey(GlobalInformation, on_delete=models.CASCADE)
	type_experience = models.CharField(max_length=5,choices=TYPE_EXPERIENCES)
	programming_languages = models.TextField(max_length=200)
	tools_used = models.TextField(max_length=200)
	description = models.TextField(max_length=1000)
	
	#for type_experience == "pro":
	starting_date = models.DateTimeField(null=True)
	ending_date = models.DateTimeField(null=True)
	job_title = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	city = models.CharField(max_length=100)

	def __str__(self):
		return f"Experience type is {self.type_experience}"

class ExperienceDetail(models.Model):
	experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
	goal = models.TextField(max_length=500)
	detail = models.TextField(max_length=1000)
	accomplishment = models.TextField(max_length=500)

	def __str__(self):
		return self.goal[:50]

class Formation(models.Model):
	language = models.ForeignKey(GlobalInformation, on_delete=models.CASCADE)
	starting_date = models.DateTimeField()
	ending_date = models.DateTimeField()
	title = models.CharField(max_length=100)
	accomplishment = models.TextField(max_length=500)

	def __str__(self):
		return self.title

class AboutMe(models.Model):
	language = models.ForeignKey(GlobalInformation, on_delete=models.CASCADE)
	description_text = models.TextField(max_length = 500)
	extra_profesionnal_sports = models.TextField(max_length = 500)
	extra_profesionnal_activity = models.CharField(max_length = 100)

