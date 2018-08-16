"""
test_rps.py

Tests for rps.
"""
from rps import app


def test_plays():
    plays = app.PLAYS
    assert isinstance(plays, list)
    assert len(plays) == 15
