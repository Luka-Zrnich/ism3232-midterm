# part 2

NO_DISCOUNT = 0.0
LOW_DISCOUNT = 0.09
HIGH_DISCOUNT = 0.14

def calculate_bean_cost(bags_price: float, bags: int) -> float:
    """Returns the bean cost before any discount (rule 1)."""
    return bags_price * bags

def get_bulk_discount(bags: int, partner: bool = False) -> float
    """Returns the discount rate as a decimal, so 9 percent is 0.09 (rules 2 and 3)."""

def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float
    """Returns the shipment total for one shipment: the discounted cost, plus the shipping fee when it applies (rule 4). It must call your first two functions."""

def requires_prepayment(total: float) -> bool
    """Returns True when the shipment total requires prepayment (rule 5), otherwise False."""

def needs_pallet(bags: int, total: float) -> bool
    """Returns True when the shipment needs a freight pallet (rule 6), otherwise False."""

def total_shipped(shipments: list) -> float
    """Returns the sum of the shipment totals for every shipment in the list. It must use a for loop that calls calculate_shipment_total."""

def largest_shipment(shipments: list) -> str
    """Returns the buyer of the shipment with the largest shipment total. If two are tied for largest, it returns the one that comes first in the list. An empty list returns an empty string"""

def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str
    """Returns one line of the report, such as Uptown Bakery: $175.00 | prepayment: no | pallet: no. Each True/False value is shown as yes or no, and the amount always has two decimal places."""
