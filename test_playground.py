"""Test unitarios para playground"""

import playground

class TestPlayground:
	def test_areacirculo(self):
		assert playground.areacirculo(4)==50.26548245743669


	def test_farenheitacelcius(self):
		assert playground.farenheitacelcius(32)==0

	def test_extensionarchivo(self):
		assert playground.extensionarchivo("luisa.pdf")=="pdf"

	def test_esparoimpar(self):
		assert playground.esparoimpar(4) == "par"
