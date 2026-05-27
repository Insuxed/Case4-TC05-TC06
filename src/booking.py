# src/booking.py

BASE_PRICE = {
    "Standard": 100.0,
    "Family": 150.0
}

SURCHARGE = {
    "Weekday": 0.0,
    "Weekend": 0.20,
    "Holiday": 0.40
}


def _validate(guest_age, room_type, booking_day, stay_duration):

    if not isinstance(guest_age, int):
        raise TypeError("guest_age must be int")

    if not (0 <= guest_age <= 120):
        raise ValueError("Invalid guest age")

    if not isinstance(stay_duration, int):
        raise TypeError("stay_duration must be int")

    if not (1 <= stay_duration <= 14):
        raise ValueError("Invalid stay duration")

    if not isinstance(room_type, str) or not room_type:
        raise ValueError("Invalid room type")

    room_type = room_type.strip().capitalize()

    if room_type not in BASE_PRICE:
        raise ValueError("Invalid room type")

    if not isinstance(booking_day, str) or not booking_day:
        raise ValueError("Invalid booking day")

    booking_day = booking_day.strip().capitalize()

    if booking_day not in SURCHARGE:
        raise ValueError("Invalid booking day")


def hotel_booking_price(
        guest_age: int,
        room_type: str,
        booking_day: str,
        stay_duration: int
) -> float:

    _validate(
        guest_age,
        room_type,
        booking_day,
        stay_duration
    )

    if guest_age < 5:
        return 0.0

    room_type = room_type.strip().capitalize()
    booking_day = booking_day.strip().capitalize()

    total = (
        BASE_PRICE[room_type]
        * (1 + SURCHARGE[booking_day])
        * stay_duration
    )

    return round(total, 2)