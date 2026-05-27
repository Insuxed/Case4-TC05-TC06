import pytest

from src.booking import hotel_booking_price


def test_TC01():
    assert hotel_booking_price(30, "Standard", "Weekday", 3) == 300.0


def test_TC02():
    assert hotel_booking_price(4, "Standard", "Weekday", 2) == 0.0






