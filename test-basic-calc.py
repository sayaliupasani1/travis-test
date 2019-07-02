import calculator

class TestCalc:

	def test_addition(self):
		assert 4 == calculator.add(2,2)

	def test_sub(self):
		assert 2 == calculator.sub(4,2)

