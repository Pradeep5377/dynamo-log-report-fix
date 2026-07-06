import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_exists():
    """Success Criterion 5: Save the report as /app/report.json."""
    assert REPORT.exists(), "report.json was not created"


def test_total_requests():
    """Success Criterion 2: Count the total number of requests."""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6


def test_unique_ips():
    """Success Criterion 3: Count the number of unique client IP addresses."""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3


def test_top_path():
    """Success Criterion 4: Determine the most frequently requested path."""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html"