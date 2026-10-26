

def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Return the food cost before any discount."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if guests < 25:
        return 0.0
    if guests < 100:
        return 0.05
    if nonprofit:
        return 0.12
    return 0.05


def calculate_event_total(
    guest_price: float,
    guests: int,
    nonprofit: bool = False
) -> float:
    """Return the event total after discount and service fee."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount)

    if discounted_cost <= 500:
        return discounted_cost + 75

    return discounted_cost


def needs_signoff(total: float) -> bool:
    """Return True when the event total exceeds $2,500."""
    return total > 2500


def needs_second_chef(guests: int, total: float) -> bool:
    """Return True when guests exceed 80 or total is at least $3,000."""
    return guests > 80 or total >= 3000


def total_booked(events: list) -> float:
    """Return the sum of all event totals."""
    total = 0.0
    for event in events:
        total += calculate_event_total(
            event["guest_price"],
            event["guests"],
            event["nonprofit"],
        )
    return total


def largest_event(events: list) -> str:
    """Return the client with the largest event total."""
    largest = ""
    largest_total = -1.0

    for event in events:
        event_total = calculate_event_total(
            event["guest_price"],
            event["guests"],
            event["nonprofit"],
        )
        if event_total > largest_total:
            largest_total = event_total
            largest = event["client"]

    return largest


def format_event_line(
    client: str,
    total: float,
    signoff: bool,
    second_chef: bool
) -> str:
    """Format one event report line."""
    signoff_text = "yes" if signoff else "no"
    chef_text = "yes" if second_chef else "no"

    return (
        f"{client}: ${total:.2f} | "
        f"sign-off: {signoff_text} | "
        f"second chef: {chef_text}"
    )
