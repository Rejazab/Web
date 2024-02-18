from django.test import TestCase

from .models import GlobalInformation, AboutMe, Experience, ExperienceDetail, Formation

"""
Test of the differents models.
Order is : 
	- GlobalInformationModelTests
	- ExperienceModelTests
	- ExperienceDetailModelTests
	- FormationModelTests
"""
class GlobalInformationModelTests(TestCase):
	def test_approriate_description_is_print(self):
		"""
		An approriate description should be return to have informations while navigating on the GUI Admin.
		"""
		informations = GlobalInformation(last_name="L name", first_name="F name", job_title="Job", mail="test@test.com", linkedin="http://test.com", github="http://test.com", codingame="http://test.com", languages = "fr")
		self.assertEqual(informations, "Global information for language fr")

class ExperienceModelTests(TestCase):
	def test_approriate_description_is_print(self)
		"""
		An approriate description should be return to have informations while navigating on the GUI Admin.
		"""
		experience = Experience()

class ExperienceDetailModelTests(TestCase):
	def test_approriate_description_is_print(self)
		"""
		An approriate description should be return to have informations while navigating on the GUI Admin.
		"""
		experience_detail = ExperienceDetail()

class FormationModelTests(TestCase):
	def test_approriate_description_is_print(self)
		"""
		An approriate description should be return to have informations while navigating on the GUI Admin.
		"""
		formation = Formation()

"""
Test of the differents views.
Order is :
- 
- 
- 
- 
"""