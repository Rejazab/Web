from django.contrib import admin
from .models import GlobalInformation, Experience, ExperienceDetail, Formation, AboutMe

class ExperienceInLine(admin.StackedInline):
	model = Experience
	readonly_fields = [
		"type_experience",
		"description",
		"job_title",
		"company",
	]
	fieldsets = [
		(None, {"fields":["type_experience"]}),
		(None, {"fields":["description"][:50]}),
		(None, {"fields":["job_title"]}),
		(None, {"fields":["company"]}),
	]

class ExperienceDetailInLine(admin.TabularInline):
	model = ExperienceDetail
	extra = 2

class FormationInLine(admin.TabularInline):
	model = Formation
	readonly_fields = [
		"title",
		"accomplishment",
	]
	fieldsets = [
		(None, {"fields":["title"]}),
		(None, {"fields":["accomplishment"]}),
	]

class AboutMeInLine(admin.TabularInline):
	model = AboutMe
	extra = 1

class GlobalInformationAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {"fields": ["languages"]}),
		(None, {"fields": ["last_name"]}),
		(None, {"fields": ["first_name"]}),
		(None, {"fields": ["job_title"]}),
		(None, {"fields": ["mail"]}),
		(None, {"fields": ["phone_number"]}),
		("Links", {"fields": ["linkedin"]}),
		(None, {"fields": ["github"]}),
		(None, {"fields": ["codingame"]}),
		]
	inlines = [
		AboutMeInLine,
		ExperienceInLine,
		FormationInLine,
	]
	list_filter = ["languages"]

class ExperienceAdmin(admin.ModelAdmin):
	inlines=[ExperienceDetailInLine]


# Register your models here.
admin.site.register(GlobalInformation, GlobalInformationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Formation)
