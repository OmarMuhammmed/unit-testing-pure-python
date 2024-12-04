import pytest
from cal_tax import calculate_tax


def test_calculate_tax_normal():
    assert calculate_tax(100, 0.15) == 115  


def test_calculate_tax_negative_values():
    with pytest.raises(ValueError):
        calculate_tax(-100, 0.15)


def test_calculate_tax_zero_tax_rate():
    assert calculate_tax(100, 0) == 100 

def test_calculate_tax_zero_price():
    assert calculate_tax(0, 0.15) == 0  
