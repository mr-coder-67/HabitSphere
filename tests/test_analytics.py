import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from habit_tracker import Analytics

def test_analytics_returns_empty_list_when_no_habits(monkeypatch):
    analytics = Analytics(database=object())

    monkeypatch.setattr(analytics, "_habit_rows", lambda user_id: [])

    result = analytics.calculate(user_id=1)

    assert result == []
def test_analytics_calculates_completion_percentage(monkeypatch):
    analytics = Analytics(database=object())

    monkeypatch.setattr(
        analytics,
        "_habit_rows",
        lambda user_id: [
            {
                "habit_id": 1,
                "habit_name": "Exercise",
                "goal_type": "daily",
                "target_count": 1,
                "start_date": __import__("datetime").date.today(),
                "status": "active",
            }
        ],
    )

    monkeypatch.setattr(
        analytics,
        "_completion_rows",
        lambda habit_id: [
            {
                "completion_date": __import__("datetime").date.today(),
                "completion_count": 1,
            }
        ],
    )

    result = analytics.calculate(user_id=1, period_days=1)

    assert result[0]["completion_percentage"] == 100
    
def test_analytics_calculates_missed_days(monkeypatch):
    analytics = Analytics(database=object())

    monkeypatch.setattr(
        analytics,
        "_habit_rows",
        lambda user_id: [
            {
                "habit_id": 1,
                "habit_name": "Exercise",
                "goal_type": "daily",
                "target_count": 1,
                "start_date": __import__("datetime").date.today(),
                "status": "active",
            }
        ],
    )

    monkeypatch.setattr(
        analytics,
        "_completion_rows",
        lambda habit_id: [],
    )

    result = analytics.calculate(user_id=1, period_days=3)

    assert result[0]["completion_percentage"] == 0
    assert result[0]["missed_days"] == 3