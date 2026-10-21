# part 4

from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    format_shipment_line,
    get_bulk_discount,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)


# 1
def test_calculate_bean_cost():
    assert calculate_bean_cost(10, 5) == 50


# 2
def test_get_bulk_discount_no_discount():
    assert get_bulk_discount(10) == 0.0


# 3
def test_get_bulk_discount_low_discount():
    assert get_bulk_discount(30) == 0.09


# 4
def test_get_bulk_discount_high_discount():
    assert get_bulk_discount(100) == 0.14


# 5
def test_get_bulk_discount_partner_discount():
    assert get_bulk_discount(30, partner=True) == 0.13


# 6
def test_calculate_shipment_total_no_discount():
    assert calculate_shipment_total(10.00, 5, partner=False) == 85


# 7
def test_calculate_shipment_total_discount_partner():
    assert calculate_shipment_total(10.00, 25, partner=True) == 252.5


# 8
def test_calculate_shipment_total_no_fee():
    assert calculate_shipment_total(10.00, 80, partner=False) == 688


# 9
def test_calculate_shipment_total_exact():
    assert calculate_shipment_total(25.00, 10, False) == 250


# 10
def test_requires_prepayment_true():
    assert requires_prepayment(1600) == True


# 11
def test_requires_prepayment_false():
    assert requires_prepayment(500) == False


# 12
def test_requires_prepayment_limit():
    assert requires_prepayment(1500) == True


# 13
def test_needs_pallet_both_true():
    assert needs_pallet(80, 800.00) == True


# 14
def test_needs_pallet_one_true():
    assert needs_pallet(80, 500.00) == False


# 15
def test_needs_pallet_limit():
    assert needs_pallet(60, 700.00) == False


# 16
def test_total_shipped():
    shipments = [
        {"bag_price": 10.00, "bags": 10, "partner": False},
        {"bag_price": 15.00, "bags": 30, "partner": False},
        {"bag_price": 12.00, "bags": 90, "partner": True},
    ]
    assert total_shipped(shipments) == 1430.1


# 17
def test_largest_shipment():
    shipments = [
        {"buyer": "GH", "bag_price": 10.00, "bags": 10, "partner": False},
        {"buyer": "LZ", "bag_price": 15.00, "bags": 30, "partner": False},
        {"buyer": "VB", "bag_price": 12.00, "bags": 90, "partner": True},
    ]
    assert largest_shipment(shipments) == "VB"


# 18
def test_largest_shipment_tie():
    shipments = [
        {"buyer": "GH", "bag_price": 10.00, "bags": 10, "partner": False},
        {"buyer": "LZ", "bag_price": 15.00, "bags": 30, "partner": False},
        {"buyer": "VB", "bag_price": 12.00, "bags": 90, "partner": True},
        {"buyer": "RI", "bag_price": 12.00, "bags": 90, "partner": True},
    ]
    assert largest_shipment(shipments) == "VB"


# 19
def test_largest_shipment_empty():
    shipments = []
    assert largest_shipment(shipments) == ""


# 20
def test_format_shipment_line():
    result = format_shipment_line("LZ", 250.00, False, False)
    assert result == "LZ: $250.00 | prepayment: no | pallet: no"
