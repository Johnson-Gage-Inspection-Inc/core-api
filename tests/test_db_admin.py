import os
import subprocess
from unittest.mock import MagicMock, Mock, patch

import pytest
from click.testing import CliRunner
from sqlalchemy.exc import SQLAlchemyError

from db_admin import (
    cli,
    create_migration,
    create_tables,
    downgrade_db,
    drop_tables,
    test_connection,
    upgrade_db,
)


@pytest.fixture
def runner():
    """Click CLI test runner."""
    return CliRunner()


@pytest.fixture
def mock_database_url():
    """Mock database URL for testing."""
    return "postgresql://user:password@localhost:5432/testdb"


@pytest.fixture
def mock_engine():
    """Mock SQLAlchemy engine."""
    engine = Mock()
    connection = MagicMock()
    result = Mock()
    result.fetchone.return_value = ["PostgreSQL 14.5"]
    connection.execute.return_value = result
    connection.__enter__.return_value = connection
    connection.__exit__.return_value = None
    engine.connect.return_value = connection
    return engine


class TestTestConnection:
    """Tests for test_connection command."""

    @patch.dict(os.environ, {}, clear=True)
    def test_missing_database_url(self, runner):
        """Test error when DATABASE_URL is not set."""
        result = runner.invoke(test_connection)

        assert result.exit_code == 1
        assert "ERROR: Please update DATABASE_URL in .env file" in result.output

    @patch.dict(
        os.environ,
        {"DATABASE_URL": "postgresql://user:YOUR_PASSWORD_HERE@localhost/db"},
    )
    def test_invalid_database_url_placeholder(self, runner):
        """Test error when DATABASE_URL contains placeholder text."""
        result = runner.invoke(test_connection)

        assert result.exit_code == 1
        assert "ERROR: Please update DATABASE_URL in .env file" in result.output

    @patch("db_admin.create_engine")
    @patch.dict(
        os.environ, {"DATABASE_URL": "postgresql://user:password@localhost:5432/testdb"}
    )
    def test_successful_connection(self, mock_create_engine, runner, mock_engine):
        """Test successful database connection."""
        mock_create_engine.return_value = mock_engine

        result = runner.invoke(test_connection)

        assert result.exit_code == 0
        assert "SUCCESS: Connected to PostgreSQL" in result.output
        assert "Version: PostgreSQL 14.5" in result.output
        mock_create_engine.assert_called_once_with(
            "postgresql://user:password@localhost:5432/testdb"
        )

    @patch("db_admin.create_engine")
    @patch.dict(
        os.environ, {"DATABASE_URL": "postgresql://user:password@localhost:5432/testdb"}
    )
    def test_connection_failure(self, mock_create_engine, runner):
        """Test database connection failure."""
        mock_create_engine.side_effect = SQLAlchemyError("Connection failed")

        result = runner.invoke(test_connection)

        assert result.exit_code == 1
        assert "ERROR: Connection failed" in result.output


class TestCreateTables:
    """Tests for create_tables command."""

    @patch.dict(os.environ, {}, clear=True)
    def test_missing_database_url(self, runner):
        """Test error when DATABASE_URL is not set."""
        result = runner.invoke(create_tables)

        assert result.exit_code == 1
        assert "ERROR: DATABASE_URL not set" in result.output

    @patch("db_admin.create_engine")
    @patch("db_admin.Base")
    @patch.dict(
        os.environ, {"DATABASE_URL": "postgresql://user:password@localhost:5432/testdb"}
    )
    def test_successful_table_creation(
        self, mock_base, mock_create_engine, runner, mock_engine
    ):
        """Test successful table creation."""
        mock_create_engine.return_value = mock_engine
        mock_base.metadata.create_all = Mock()

        result = runner.invoke(create_tables)

        assert result.exit_code == 0
        assert "SUCCESS: All tables created" in result.output
        mock_base.metadata.create_all.assert_called_once_with(mock_engine)

    @patch("db_admin.create_engine")
    @patch("db_admin.Base")
    @patch.dict(
        os.environ, {"DATABASE_URL": "postgresql://user:password@localhost:5432/testdb"}
    )
    def test_table_creation_failure(self, mock_base, mock_create_engine, runner):
        """Test table creation failure."""
        mock_create_engine.return_value = Mock()
        mock_base.metadata.create_all.side_effect = SQLAlchemyError(
            "Table creation failed"
        )

        result = runner.invoke(create_tables)

        assert result.exit_code == 1
        assert "ERROR: Table creation failed" in result.output


class TestDropTables:
    """Tests for drop_tables command."""

    @patch.dict(os.environ, {}, clear=True)
    def test_missing_database_url(self, runner):
        """Test error when DATABASE_URL is not set after confirmation."""
        result = runner.invoke(drop_tables, input="y\n")

        assert result.exit_code == 1
        assert "ERROR: DATABASE_URL not set" in result.output

    def test_user_cancellation(self, runner):
        """Test user cancels operation."""
        result = runner.invoke(drop_tables, input="n\n")

        assert result.exit_code == 0
        assert "Cancelled." in result.output

    @patch("db_admin.create_engine")
    @patch("db_admin.Base")
    @patch.dict(
        os.environ, {"DATABASE_URL": "postgresql://user:password@localhost:5432/testdb"}
    )
    def test_successful_table_drop(
        self, mock_base, mock_create_engine, runner, mock_engine
    ):
        """Test successful table dropping."""
        mock_create_engine.return_value = mock_engine
        mock_base.metadata.drop_all = Mock()

        result = runner.invoke(drop_tables, input="y\n")

        assert result.exit_code == 0
        assert "SUCCESS: All tables dropped" in result.output
        mock_base.metadata.drop_all.assert_called_once_with(mock_engine)

    @patch("db_admin.create_engine")
    @patch("db_admin.Base")
    @patch.dict(
        os.environ, {"DATABASE_URL": "postgresql://user:password@localhost:5432/testdb"}
    )
    def test_table_drop_failure(self, mock_base, mock_create_engine, runner):
        """Test table dropping failure."""
        mock_create_engine.return_value = Mock()
        mock_base.metadata.drop_all.side_effect = SQLAlchemyError("Drop failed")

        result = runner.invoke(drop_tables, input="y\n")

        assert result.exit_code == 1
        assert "ERROR: Drop failed" in result.output


class TestCreateMigration:
    """Tests for create_migration command."""

    @patch("db_admin.subprocess.run")
    def test_successful_migration_creation(self, mock_run, runner):
        """Test successful migration creation."""
        mock_run.return_value = None

        result = runner.invoke(create_migration, ["--message", "Add new table"])

        assert result.exit_code == 0
        assert "SUCCESS: Migration created with message: Add new table" in result.output
        mock_run.assert_called_once_with(
            ["alembic", "revision", "--autogenerate", "-m", "Add new table"], check=True
        )

    @patch("db_admin.subprocess.run")
    def test_migration_creation_failure(self, mock_run, runner):
        """Test migration creation failure."""
        mock_run.side_effect = subprocess.CalledProcessError(1, "alembic")

        result = runner.invoke(create_migration, ["--message", "Add new table"])

        assert result.exit_code == 1
        assert "ERROR: Migration creation failed" in result.output

    def test_missing_message_parameter(self, runner):
        """Test error when message parameter is missing."""
        result = runner.invoke(create_migration)

        assert result.exit_code == 2  # Click exits with 2 for missing required options
        assert "Error: Missing option '--message'" in result.output


class TestUpgradeDb:
    """Tests for upgrade_db command."""

    @patch("db_admin.subprocess.run")
    def test_successful_upgrade(self, mock_run, runner):
        """Test successful database upgrade."""
        mock_run.return_value = None

        result = runner.invoke(upgrade_db)

        assert result.exit_code == 0
        assert "SUCCESS: Database upgraded to latest migration" in result.output
        mock_run.assert_called_once_with(["alembic", "upgrade", "head"], check=True)

    @patch("db_admin.subprocess.run")
    def test_upgrade_failure(self, mock_run, runner):
        """Test database upgrade failure."""
        mock_run.side_effect = subprocess.CalledProcessError(1, "alembic")

        result = runner.invoke(upgrade_db)

        assert result.exit_code == 1
        assert "ERROR: Database upgrade failed" in result.output


class TestDowngradeDb:
    """Tests for downgrade_db command."""

    def test_user_cancellation(self, runner):
        """Test user cancels downgrade operation."""
        result = runner.invoke(downgrade_db, input="n\n")

        assert result.exit_code == 0
        assert "Cancelled." in result.output

    @patch("db_admin.subprocess.run")
    def test_successful_downgrade(self, mock_run, runner):
        """Test successful database downgrade."""
        mock_run.return_value = None

        result = runner.invoke(downgrade_db, input="y\n")

        assert result.exit_code == 0
        assert "SUCCESS: Database downgraded by one migration" in result.output
        mock_run.assert_called_once_with(["alembic", "downgrade", "-1"], check=True)

    @patch("db_admin.subprocess.run")
    def test_downgrade_failure(self, mock_run, runner):
        """Test database downgrade failure."""
        mock_run.side_effect = subprocess.CalledProcessError(1, "alembic")

        result = runner.invoke(downgrade_db, input="y\n")

        assert result.exit_code == 1
        assert "ERROR: Database downgrade failed" in result.output


class TestCliGroup:
    """Tests for the main CLI group."""

    def test_cli_help(self, runner):
        """Test CLI help output."""
        result = runner.invoke(cli, ["--help"])

        assert result.exit_code == 0
        assert "Database administration commands." in result.output

    def test_command_listing(self, runner):
        """Test that all commands are listed."""
        result = runner.invoke(cli, ["--help"])

        assert "test-connection" in result.output
        assert "create-tables" in result.output
        assert "drop-tables" in result.output
        assert "create-migration" in result.output
        assert "upgrade-db" in result.output
        assert "downgrade-db" in result.output


# Integration-style tests
class TestCommandIntegration:
    """Integration tests for command combinations."""

    @patch("db_admin.subprocess.run")
    @patch("db_admin.create_engine")
    @patch("db_admin.Base")
    @patch.dict(
        os.environ, {"DATABASE_URL": "postgresql://user:password@localhost:5432/testdb"}
    )
    def test_full_setup_workflow(
        self, mock_base, mock_create_engine, mock_run, runner, mock_engine
    ):
        """Test a complete setup workflow: create tables, create migration, upgrade."""
        mock_create_engine.return_value = mock_engine
        mock_base.metadata.create_all = Mock()
        mock_run.return_value = None

        # Create tables
        result1 = runner.invoke(create_tables)
        assert result1.exit_code == 0

        # Create migration
        result2 = runner.invoke(create_migration, ["--message", "Initial setup"])
        assert result2.exit_code == 0

        # Upgrade database
        result3 = runner.invoke(upgrade_db)
        assert result3.exit_code == 0

        # Verify all operations succeeded
        assert "SUCCESS: All tables created" in result1.output
        assert "SUCCESS: Migration created" in result2.output
        assert "SUCCESS: Database upgraded" in result3.output
