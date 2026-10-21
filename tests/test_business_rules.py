# part 4

from business_rules import calculate_bean_cost, get_bulk_discount, calculate_shipment_total, requires_prepayment, needs_pallet, total_shipped, largest_shipment, format_shipment_line

#1
def test_calculate_bean_cost():
    assert calculate_bean_cost(10, 5) == 50

#2
def test_get_bulk_discount_no_discount():
    assert get_bulk_discount(10) == 0.0

#3
def test_get_bulk_discount_low_discount():
    assert get_bulk_discount(30) == 0.09

#4
def test_get_bulk_discount_high_discount():
    assert get_bulk_discount(100) == 0.14

#5
def test_get_bulk_discount_partner_discount():
    assert get_bulk_discount(30, partner=True) == 0.13

#6
def test_calculate_shipment_total_no_discount():
    assert calculate_shipment_total(10.00, 5, partner=False) = 85

#7
def test_calculate_shipment_total_discount_partner():
    assert calculate_shipment_total(10.00, 25, partner=True) = 282.5

#8
def test_calculate_shipment_total_no_fee():
    assert calculate_shipment_total(10.00, 80, partner=False) = 912

#9
def test_calculate_shipment_total_exact():
    assert calculate_shipment_total(25.00, 10, False) = 250

#10
def test_requires_prepayment_true():
    assert requires_prepayment(1600) = True

#11
def test_requires_prepayment_false():
    assert requires_prepayment(500) = False

#12
def test_requires_prepayment_limit():
    assert requires_prepayment(1500) = True

#13
