import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from scraper import parse_headings


def test_parse_headings_basic():
    html = "<h1>Title</h1><h2>Sub</h2>"
    assert parse_headings(html) == [("h1", "Title"), ("h2", "Sub")]


def test_parse_headings_empty():
    assert parse_headings("") == []


def test_parse_headings_no_headings():
    assert parse_headings("<p>text</p>") == []
