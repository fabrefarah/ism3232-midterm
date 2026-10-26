
from business_rules import (
    calculate_food_cost,
    get_event_discount,
    calculate_event_total,
    needs_signoff,
    needs_second_chef,
    total_booked,
    largest_event,
    format_event_line,
)


# 1. Test food cost
def test_food_cost():
    assert calculate_food_cost(18.00, 20) == 360.00


# 2. Test food cost with one guest
def test_food_cost_one_guest():
    assert calculate_food_cost(25.00, 1) == 25.00


# 3. Test no discount under 25 guests
def test_discount_under_25():
    assert get_event_discount(24, False) == 0.0


# 4. Test discount at exactly 25 guests
def test_discount_boundary_25():
    assert get_event_discount(25, False) == 0.05


# 5. Test regular discount at 100 guests
def test_discount_regular_100():
    assert get_event_discount(100, False) == 0.05


# 6. Test nonprofit discount at 100 guests
def test_discount_nonprofit_100():
    assert get_event_discount(100, True) == 0.12


# 7. Test event total includes the service fee
def test_total_includes_service_fee():
    assert round(calculate_event_total(18.00, 20), 2) == 435.00


# 8. Test event total with a regular discount
def test_total_with_discount():
    assert round(calculate_event_total(22.00, 40), 2) == 836.00


# 9. Test event total with nonprofit discount
def test_total_nonprofit():
    assert round(calculate_event_total(25.00, 150, True), 2) == 3300.00


# 10. Test manager approval over the limit
def test_signoff_over_limit():
    assert needs_signoff(2500.01) is True


# 11. Test manager approval under the limit
def test_signoff_under_limit():
    assert needs_signoff(2000.00) is False


# 12. Test manager approval exactly at the limit
def test_signoff_boundary():
    assert needs_signoff(2500.00) is False


# 13. Test second chef required over 80 guests
def test_second_chef_over_guest_limit():
    assert needs_second_chef(81, 1000.00) is True


# 14. Test second chef not required under both limits
def test_second_chef_under_limits():
    assert needs_second_chef(80, 2999.99) is False


# 15. Test second chef required at the total limit
def test_second_chef_boundary_total():
    assert needs_second_chef(80, 3000.00) is True


# 16. Test total booked for multiple events
def test_total_booked():
    events = [
        {
            "client": "Finch Law",
            "guest_price": 18.00,
            "guests": 20,
            "nonprofit": False,
        },
        {
            "client": "Juniper Spa",
            "guest_price": 16.00,
            "guests": 30,
            "nonprofit": False,
        },
    ]
    assert round(total_booked(events), 2) == 966.00


# 17. Test total booked with an empty list
def test_total_booked_empty():
    assert total_booked([]) == 0.0


# 18. Test largest event
def test_largest_event():
    events = [
        {
            "client": "Finch Law",
            "guest_price": 18.00,
            "guests": 20,
            "nonprofit": False,
        },
        {
            "client": "Hilltop Gym",
            "guest_price": 30.00,
            "guests": 120,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "Hilltop Gym"


# 19. Test largest event with an empty list
def test_largest_event_empty():
    assert largest_event([]) == ""


# 20. Test formatted event report line
def test_format_event_line():
    result = format_event_line("Finch Law", 435.00, False, False)
    assert result == (
        "Finch Law: $435.00 | sign-off: no | second chef: no"
    )
