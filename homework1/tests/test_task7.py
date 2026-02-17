from src.task7 import build_url


def test_url():
    result = build_url("https://example.com", {"name": "john", "id": 1})
    assert result == "https://example.com/?name=john&id=1"

