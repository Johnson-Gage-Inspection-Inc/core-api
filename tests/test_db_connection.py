#!/usr/bin/env python3
# test_db_connection.py
"""
Test database connection utility.
Run this to verify your DATABASE_URL is correct before running migrations.
"""

import os
import sys

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


def test_connection():
    """Test the database connection."""
    load_dotenv()

    # Skip test if running in GitHub Actions CI environment
    if os.getenv("GITHUB_ACTIONS") == "true":
        pytest.skip("Skipping database connection test in CI environment")

    database_url = os.getenv("DATABASE_URL")
    if not database_url or "YOUR_PASSWORD_HERE" in database_url:
        print(
            "❌ ERROR: Please update DATABASE_URL in .env file with actual credentials"
        )
        assert False, "DATABASE_URL not properly configured"

    print(
        f"🔗 Testing connection to: {database_url.split('@')[1] if '@' in database_url else 'database'}"
    )
    try:
        engine = create_engine(database_url)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()
            print("✅ SUCCESS: Connected to PostgreSQL")
            print(f"📊 Version: {version}")

            # Test table creation permissions
            conn.execute(text("CREATE TEMP TABLE test_permissions (id int)"))
            print("✅ SUCCESS: Can create tables")

            # Use assertion instead of return for pytest
            assert True

    except Exception as e:
        print("❌ ERROR: Connection failed")
        print(f"Details: {str(e)}")
        # Use assertion instead of return for pytest
        assert False, f"Database connection failed: {str(e)}"


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
