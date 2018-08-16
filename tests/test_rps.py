"""
test_rps.py

Tests for rps.
"""
import logging

from rps import app

logging.disable(logging.CRITICAL)


def test_main(capfd):
    app.main()
    output = capfd.readouterr()[0]
    assert output.strip() == "Successfully installed your project file: rps"
