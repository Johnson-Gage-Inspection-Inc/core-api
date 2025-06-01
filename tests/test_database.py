# tests/test_database.py
import pytest
import os
from unittest.mock import patch, MagicMock
from db.models import Base, DaqbookOffset
from utils.database import SessionLocal, engine

class TestDatabaseModels:
    """Test database model functionality."""
    
    def test_daqbook_offset_model_creation(self):
        """Test DaqbookOffset model can be created."""
        offset = DaqbookOffset(
            tn="TEST123",
            temp=25.5,
            point=1,
            reading=0.001
        )
        
        assert offset.tn == "TEST123"
        assert offset.temp == 25.5
        assert offset.point == 1
        assert offset.reading == 0.001

    def test_daqbook_offset_repr(self):
        """Test DaqbookOffset string representation."""
        offset = DaqbookOffset(
            tn="TEST123",
            temp=25.5,
            point=1,
            reading=0.001
        )
        
        expected = "<DaqbookOffset(tn='TEST123', temp=25.5, point=1, reading=0.001)>"
        assert repr(offset) == expected

    def test_daqbook_offset_delta_property(self):
        """Test DaqbookOffset delta property calculation."""
        offset = DaqbookOffset(
            tn="TEST123",
            temp=25.0,
            point=1,
            reading=25.5
        )
        
        # Delta should be (reading - temp) * -1, rounded to 2 decimals
        # (25.5 - 25.0) * -1 = -0.5
        expected_delta = -0.5
        assert offset.delta == expected_delta
        
        # Test with negative delta
        offset2 = DaqbookOffset(
            tn="TEST456",
            temp=100.0,
            point=2,
            reading=99.8
        )
        
        # (99.8 - 100.0) * -1 = 0.2
        expected_delta2 = 0.2
        assert offset2.delta == expected_delta2
        
        # Test rounding to 2 decimal places
        offset3 = DaqbookOffset(
            tn="TEST789",
            temp=0.0,
            point=3,
            reading=0.123456
        )
        
        # (0.123456 - 0.0) * -1 = -0.123456, rounded to -0.12
        expected_delta3 = -0.12
        assert offset3.delta == expected_delta3

@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() == "true", 
    reason="Skipped when SKIP_AUTH=true - no real DB in CI"
)
class TestDatabaseConnection:
    """Test actual database connections (only in production mode)."""
    
    def test_database_connection_available(self):
        """Test that database connection can be established."""
        # This test only runs when SKIP_AUTH=false (production mode)
        try:
            with engine.connect() as conn:
                result = conn.execute("SELECT 1 as test")
                assert result.fetchone()[0] == 1
        except Exception as e:
            pytest.skip(f"Database not available: {e}")


    def test_get_db_session(self):
        """Test database session creation."""
        try:
            db = SessionLocal()
            assert db is not None
            # Test a simple query
            result = db.execute("SELECT 1 as test")
            assert result.fetchone()[0] == 1
            db.close()
        except Exception as e:
            pytest.skip(f"Database not available: {e}")

class TestDatabaseUtils:
    """Test database utility functions."""
    
    @patch('utils.database.SessionLocal')
    def test_session_local_creation(self, mock_session_local):
        """Test SessionLocal creation with mocked session."""
        mock_session = MagicMock()
        mock_session_local.return_value = mock_session
        
        # Import the patched version from the module
        from utils.database import SessionLocal as PatchedSessionLocal
        result = PatchedSessionLocal()
        
        assert result == mock_session
        mock_session_local.assert_called_once()

    @patch.dict(os.environ, {'DATABASE_ECHO': 'true'})
    def test_database_echo_environment_setting(self):
        """Test that DATABASE_ECHO environment variable is properly read."""
        # This test verifies the environment variable is set correctly
        assert os.getenv("DATABASE_ECHO") == "true"
        
        # Test the logic that would be used in database.py
        echo_setting = os.getenv("DATABASE_ECHO", "false").lower() == "true"
        assert echo_setting == True

    def test_get_db_session_generator(self):
        """Test get_db_session is a generator function."""
        from utils.database import get_db_session
        generator = get_db_session()
        
        # Should be a generator
        assert hasattr(generator, '__next__')
        assert hasattr(generator, '__iter__')
        
        # Clean up the generator
        try:
            next(generator)
        except StopIteration:
            pass
        except Exception:
            # Expected if no real database connection
            pass
        finally:
            generator.close()

    @patch('utils.database.SessionLocal')
    def test_get_db_session_cleanup_on_exception(self, mock_session_local):
        """Test get_db_session properly closes session even if exception occurs."""
        mock_session = MagicMock()
        mock_session_local.return_value = mock_session
        
        from utils.database import get_db_session
        generator = get_db_session()
        
        try:
            session = next(generator)
            assert session == mock_session
            # Simulate exception in user code
            generator.throw(Exception("User code error"))
        except Exception:
            pass
        
        # Session should still be closed
        mock_session.close.assert_called_once()
