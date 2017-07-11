import mathlib
import pytest

@pytest.mark.skip(reason=" testing the skip feature of pytest")
def test_calc_total():
    total = mathlib.calc_total(4,5)
    assert total == 9

def test_calc_multiply():
    result = mathlib.calc_multiply(4,5)
    assert result == 20