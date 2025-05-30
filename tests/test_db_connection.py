#!/usr/bin/env python3
# test_db_connection.py
"""
Test database connection utility.
Run this to verify your DATABASE_URL is correct before running migrations.
"""

import os
import sys
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

def test_connection():
    """Test the database connection."""
    load_dotenv()
    
    database_url = os.getenv("DATABASE_URL")
    if not database_url or "YOUR_PASSWORD_HERE" in database_url:
        print("❌ ERROR: Please update DATABASE_URL in .env file with actual credentials")
        return False
    
    print(f"🔗 Testing connection to: {database_url.split('@')[1] if '@' in database_url else 'database'}")
    
    try:
        engine = create_engine(database_url)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            print(f"✅ SUCCESS: Connected to PostgreSQL")
            print(f"📊 Version: {version}")
            
            # Test table creation permissions
            conn.execute(text("CREATE TEMP TABLE test_permissions (id int)"))
            print("✅ SUCCESS: Can create tables")
            
            return True
            
    except Exception as e:
        print(f"❌ ERROR: Connection failed")
        print(f"Details: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
