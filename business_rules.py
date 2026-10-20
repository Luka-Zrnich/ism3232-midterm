# part 1

calculate_license_cost(seat_price: float, seats: int) -> float

get_seat_discount(seats: int, education: bool = False) -> float

calculate_license_total(seat_price: float, seats: int, education: bool = False) -> float

needs_contract_review(total: float) -> bool

gets_trainer(seats: int, total: float) -> bool

total_licensed(orders: list) -> float

largest_license(orders: list) -> str

format_license_line(company: str, total: float, contract_review: bool, trainer: bool) -> str
