import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from habit_tracker import HabitTracker


def test_valid_completion_date_is_parsed():
    result = HabitTracker._parse_date("2026-08-21")

    assert result.isoformat() == "2026-08-21"


def test_invalid_completion_date_is_rejected():
    with pytest.raises(ValueError, match="A valid completion date is required"):
        HabitTracker._parse_date("invalid-date")
        
def test_invalid_completion_date_empty_value_is_rejected():
    with pytest.raises(ValueError, match="A valid completion date is required"):
        HabitTracker._parse_date("")

def test_invalid_habit_id_is_rejected_before_database_access():
    tracker = HabitTracker(database=object())

    with pytest.raises(ValueError, match="Invalid completion values"):
        tracker.record_completion(
            user_id=1,
            payload={
                "habit_id": 0,
                "completion_count": 1,
                "completion_date": "2026-08-21",
                "completed": True,
            },
        )
def test_completed_habit_requires_completion_count():
    tracker = HabitTracker(database=object())

    with pytest.raises(ValueError, match="Completed habits need a count of at least 1"):
        tracker.record_completion(
            user_id=1,
            payload={
                "habit_id": 1,
                "completion_count": 0,
                "completion_date": "2026-08-21",
                "completed": True,
            },
        )