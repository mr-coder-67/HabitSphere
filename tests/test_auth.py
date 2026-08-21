import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from habit_tracker import PasswordManager


def test_password_hash_is_not_plaintext():
    password = "SecurePassword123"
    hashed_password = PasswordManager.hash_password(password)

    assert hashed_password != password


def test_correct_password_is_verified():
    password = "SecurePassword123"
    hashed_password = PasswordManager.hash_password(password)

    assert PasswordManager.verify_password(password, hashed_password) is True


def test_incorrect_password_is_rejected():
    hashed_password = PasswordManager.hash_password("CorrectPassword123")

    assert PasswordManager.verify_password(
        "WrongPassword123",
        hashed_password
    ) is False


def test_invalid_hash_is_rejected():
    assert PasswordManager.verify_password(
        "SecurePassword123",
        "invalid_hash"
    ) is False