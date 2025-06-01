#!/usr/bin/env python3
# db_admin.py
"""
Database administration utility for JGI Flask API.
Provides commands for database setup, migrations, and data management.
"""

import os
import subprocess
import sys

import click
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

from db.models import Base

# Load environment variables
load_dotenv()


@click.group()
def cli():
    """Database administration commands."""
    pass


@cli.command()
def test_connection():
    """Test database connection."""
    database_url = os.getenv("DATABASE_URL")
    if not database_url or "YOUR_PASSWORD_HERE" in database_url:
        click.echo("❌ ERROR: Please update DATABASE_URL in .env file", err=True)
        sys.exit(1)

    try:
        engine = create_engine(database_url)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            click.echo("✅ SUCCESS: Connected to PostgreSQL")
            click.echo(f"📊 Version: {version}")
    except Exception as e:
        click.echo(f"❌ ERROR: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
def create_tables():
    """Create all tables (for development only - use alembic for production)."""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        click.echo("❌ ERROR: DATABASE_URL not set", err=True)
        sys.exit(1)

    try:
        engine = create_engine(database_url)
        Base.metadata.create_all(engine)
        click.echo("✅ SUCCESS: All tables created")
    except Exception as e:
        click.echo(f"❌ ERROR: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
def drop_tables():
    """Drop all tables (DANGEROUS - for development only)."""
    if not click.confirm("⚠️  WARNING: This will DELETE ALL DATA. Continue?"):
        click.echo("Cancelled.")
        return

    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        click.echo("❌ ERROR: DATABASE_URL not set", err=True)
        sys.exit(1)

    try:
        engine = create_engine(database_url)
        Base.metadata.drop_all(engine)
        click.echo("✅ SUCCESS: All tables dropped")
    except Exception as e:
        click.echo(f"❌ ERROR: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.option("--message", "-m", required=True, help="Migration message")
def create_migration(message):
    """Create a new Alembic migration."""
    try:
        subprocess.run(
            ["alembic", "revision", "--autogenerate", "-m", message], check=True
        )
        click.echo(f"✅ SUCCESS: Migration created with message: {message}")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ ERROR: Migration creation failed: {e}", err=True)
        sys.exit(1)


@cli.command()
def upgrade_db():
    """Apply all pending migrations."""
    try:
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        click.echo("✅ SUCCESS: Database upgraded to latest migration")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ ERROR: Database upgrade failed: {e}", err=True)
        sys.exit(1)


@cli.command()
def downgrade_db():
    """Downgrade database by one migration."""
    if not click.confirm("⚠️  WARNING: This will revert the last migration. Continue?"):
        click.echo("Cancelled.")
        return
    try:
        subprocess.run(["alembic", "downgrade", "-1"], check=True)
        click.echo("✅ SUCCESS: Database downgraded by one migration")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ ERROR: Database downgrade failed: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    cli()
