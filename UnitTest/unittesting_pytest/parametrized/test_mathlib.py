import pytest
import mathlib

@pytest.mark.parametrize("input_param, output_param",[
			(5, 25), (9, 81), (10, 100)
			])
def test_calc_square(input_param, output_param):
	result = mathlib.calc_square(input_param)
	assert result == output_param