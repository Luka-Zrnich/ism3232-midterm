# part 3

from business_rules import (
    calculate_shipment_total,
    format_shipment_line,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)

shipments = [
    {"buyer": "Uptown Bakery", "bag_price": 14.00, "bags": 10, "partner": False},
    {"buyer": "Vine Cafe", "bag_price": 12.50, "bags": 15, "partner": True},
    {"buyer": "Wren Hotel", "bag_price": 13.00, "bags": 40, "partner": False},
    {"buyer": "Yarrow Cafe", "bag_price": 12.00, "bags": 50, "partner": True},
    {"buyer": "Zenith Grocers", "bag_price": 11.00, "bags": 200, "partner": False},
    {"buyer": "Alder Hotel", "bag_price": 12.00, "bags": 60, "partner": False},
    {"buyer": "Birch Diner", "bag_price": 11.00, "bags": 61, "partner": False},
    {"buyer": "Cove Market", "bag_price": 13.00, "bags": 150, "partner": True},
]

for shipment in shipments:
    total = calculate_shipment_total(
        shipment["bag_price"], shipment["bags"], shipment["partner"]
    )
    prepayment = requires_prepayment(total)
    pallet = needs_pallet(shipment["bags"], total)
    print(format_shipment_line(shipment["buyer"], total, prepayment, pallet))
print(f"Total shipped: ${total_shipped(shipments):.2f}")
print(f"Average shipment: ${total_shipped(shipments) / len(shipments):,.2f}")
print(f"Largest shipment: {largest_shipment(shipments)}")
print(
    f"Prepayments required: {sum(1 for shipment in shipments if requires_prepayment(calculate_shipment_total(shipment['bag_price'], shipment['bags'], shipment['partner'])))}"
)
print(
    f"Pallets needed: {sum(1 for shipment in shipments if needs_pallet(shipment['bags'], calculate_shipment_total(shipment['bag_price'], shipment['bags'], shipment['partner'])))}"
)
