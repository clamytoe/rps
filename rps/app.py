#!/usr/bin/env python3
"""
app.py

Rock, Paper, Scissor's +
"""
from .log_init import setup_logging

logger = setup_logging()


def main():
    logger.debug("Entering main.")
    logger.info("Printing default message")
    print(f"Successfully installed your project file: rps")


if __name__ == "__main__":
    logger.debug("Running as a module.")
    main()
