"""
Run this script once to create all tables in your PostgreSQL database.
Make sure your .env file is configured before running.

Usage:
    python init_db.py
"""

from database import engine, Base
import models  # noqa: F401 — imports needed so Base registers all models


def init():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Done. Tables created successfully.")


if __name__ == "__main__":
    init()
