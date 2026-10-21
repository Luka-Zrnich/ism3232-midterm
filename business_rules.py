# part 2
# Luka Zrnich

NO_DISCOUNT = 0.0
LOW_DISCOUNT = 0.09
HIGH_DISCOUNT = 0.14
PARTNER_DISCOUNT = 0.04
PREPAYMENT_REQUIREMENT = 1500

def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Returns the bean cost before any discount (rule 1)."""
    return bag_price * bags

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Returns the discount rate as a decimal, so 9 percent is 0.09 (rules 2 and 3)."""
    if bags < 20:
        return NO_DISCOUNT
    elif bags <80:
        discount = LOW_DISCOUNT
    elif bags >= 80:
        discount = HIGH_DISCOUNT
    if partner:
        discount += PARTNER_DISCOUNT
    return discount
    
def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
    """Returns the shipment total for one shipment: the discounted cost, plus the shipping fee when it applies (rule 4). It must call your first two functions."""
    bean_cost = calculate_bean_cost(bag_price, bags)
    discount = get_bulk_discount(bags, partner)
    if bean_cost - (bean_cost * discount) < 250:
        return bean_cost - (bean_cost * discount) + 35
    else:
        return bean_cost - (bean_cost * discount)

def requires_prepayment(total: float) -> bool:
    """Returns True when the shipment total requires prepayment (rule 5), otherwise False."""
    return total >= PREPAYMENT_REQUIREMENT

def needs_pallet(bags: int, total: float) -> bool:
    """Returns True when the shipment needs a freight pallet (rule 6), otherwise False."""
    return bags > 60 and total > 700

def total_shipped(shipments: list) -> float:
    """Returns the sum of the shipment totals for every shipment in the list. It must use a for loop that calls calculate_shipment_total."""
    total = 0
    for shipment in shipments:
        total += calculate_shipment_total(shipment["bag_price"], shipment["bags"], shipment["partner"])
    return total

def largest_shipment(shipments: list) -> str:
    """Returns the buyer of the shipment with the largest shipment total. If two are tied for largest, it returns the one that comes first in the list. An empty list returns an empty string"""
    largest = 0
    buyer = ""
    for shipment in shipments:
        if calculate_shipment_total(shipment["bag_price"], shipment["bags"], shipment["partner"]) > largest:
            largest = calculate_shipment_total(shipment["bag_price"], shipment["bags"], shipment["partner"])
            buyer = shipment["buyer"]
    return buyer

def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:
    """Returns one line of the report, such as Uptown Bakery: $175.00 | prepayment: no | pallet: no. Each True/False value is shown as yes or no, and the amount always has two decimal places."""
    return f"{buyer}: ${total:.2f} | prepayment: {'yes' if prepayment else 'no'} | pallet: {'yes' if pallet else 'no'}"
