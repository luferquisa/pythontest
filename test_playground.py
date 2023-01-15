"""Test unitarios para playground"""

import playground

class TestPlayground:
	def test_areacirculo(self):
		assert playground.areacirculo(4)==50.26548245743669


	def test_farenheitacelcius(self):
		assert playground.farenheitacelcius(32)==0
