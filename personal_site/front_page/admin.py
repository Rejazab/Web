from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import GlobalInformation, Experience, ExperienceDetail, Formation, AboutMe


text_field_rows = 10
text_field_cols = 400

class ExperienceInLine(admin.TabularInline):
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

class ExperienceDetailInLine(admin.StackedInline):
	model = ExperienceDetail
	extra = 2

	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':text_field_rows, 'cols':text_field_cols})},
	}

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

class AboutMeInLine(admin.StackedInline):
	model = AboutMe
	extra = 1

	fieldsets = [
		(None,
			{
				"classes": ["wide"],
				"fields": ["description_text", "extra_profesionnal_sports", "extra_profesionnal_activity"],
			},
		),
	]

	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':text_field_rows, 'cols':text_field_cols})},
	}

class GlobalInformationAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {"fields": ["languages", ("last_name", "first_name"), "job_title", "mail"]}),
		("Links", {"fields": ["linkedin", "github", "codingame"]}),
		]

	inlines = [
		AboutMeInLine,
		ExperienceInLine,
		FormationInLine,
	]
	list_filter = ["languages"]

class ExperienceAdmin(admin.ModelAdmin):
	inlines=[ExperienceDetailInLine]

	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': Textarea(attrs={'rows':text_field_rows, 'cols':text_field_cols})},
	}

	list_filter = ["type_experience"]

class FormationAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':text_field_rows, 'cols':text_field_cols})},
	}

	list_filter = ["starting_date"]

# Register your models here.
admin.site.register(GlobalInformation, GlobalInformationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Formation, FormationAdmin)
