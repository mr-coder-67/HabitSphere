import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from habit_tracker import User


def test_valid_registration_data_is_cleaned():
    name, email = User.validate_registration(
        "  Akhil Shaik  ",
        "  AKHIL@example.com  ",
        "password123"
    )

    assert name == "Akhil Shaik"
    assert email == "akhil@example.com"


def test_short_name_is_rejected():
    with pytest.raises(ValueError, match="Full name must contain"):
        User.validate_registration(
            "A",
            "user@example.com",
            "password123"
        )


def test_invalid_email_is_rejected():
    with pytest.raises(ValueError, match="Enter a valid email address"):
        User.validate_registration(
            "Akhil Shaik",
            "invalid-email",
            "password123"
        )


def test_short_password_is_rejected():
    with pytest.raises(
        ValueError,
        match="Password must contain at least 8 characters"
    ):
        User.validate_registration(
            "Akhil Shaik",
            "user@example.com",
            "short"
        )