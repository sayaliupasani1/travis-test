import calculator

class TestCalc:

	def test_addition(self):
		assert 6 == calculator.add(2,2,2)

	def test_sub(self):
		assert 2 == calculator.sub(4,2)

	def test_multiply(self):
		assert 4 == calculator.multiply(2,2)

	def test_divide(self):
		assert 2 == calculator.divide(4,2)
