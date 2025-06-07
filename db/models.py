# db/models.py
import json

from sqlalchemy import Column, DateTime, Integer, Numeric, Text, UniqueConstraint, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DaqbookOffset(Base):
    __tablename__ = "daqbook_offsets"

    id = Column(Integer, primary_key=True)
    tn = Column(Text, nullable=False)
    temp = Column(Numeric, nullable=False)
    point = Column(Integer, nullable=False)
    reading = Column(Numeric, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "tn", "temp", "point", name="uq_daqbook_offsets_tn_temp_point"
        ),
    )

    @property
    def delta(self):
        """Calculate delta as (reading - temp) * -1, rounded to 2 decimal places."""
        return round((float(self.reading) - float(self.temp)) * -1, 2)

    def __repr__(self):
        return f"<DaqbookOffset(tn='{self.tn}', temp={self.temp}, point={self.point}, reading={self.reading})>"


class WireOffset(Base):
    """
    Append-only table for wire correction factors by temperature.

    This table stores wire correction factors for each wire lot (traceability number)
    at different nominal temperatures. Each record represents a measurement from
    a wire certificate Excel file with full audit trail.

    Use wire_offsets_current view for the most recent correction factors.
    """

    __tablename__ = "wire_offsets"

    id = Column(Integer, primary_key=True)
    traceability_no = Column(
        Text, nullable=False
    )  # Wire lot identifier (e.g., "072513A")
    nominal_temp = Column(
        Numeric(precision=8, scale=2), nullable=False
    )  # Temperature in Celsius
    correction_factor = Column(
        Numeric(precision=10, scale=6), nullable=False
    )  # Wire correction factor
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_by = Column(
        Text, nullable=True
    )  # SharePoint user who last modified the source file

    def __repr__(self):
        return f"<WireOffset(id={self.id}, traceability_no='{self.traceability_no}', temp={self.nominal_temp}, cf={self.correction_factor})>"


class WireSetCert(Base):
    """
    Cached data from WireSetCerts.xlsx for mapping serial numbers to wire sets.

    This table caches the complete WireSetCerts.xlsx data from SharePoint.
    It maps individual wire serial numbers (like 'J201') to their wire set groups
    and includes all certification metadata.
    Should be refreshed periodically or on-demand via API.
    """

    __tablename__ = "wire_set_certs"

    id = Column(Integer, primary_key=True)
    serial_number = Column(Text, nullable=False, unique=True)  # e.g. "J201"
    wire_set_group = Column(Text, nullable=False)  # e.g. "J201-J214"

    # Additional fields from WireSetCerts.xlsx
    asset_id = Column(Integer, nullable=True)  # Asset ID number
    asset_tag = Column(Text, nullable=True)  # Asset tag identifier
    custom_order_number = Column(Text, nullable=True)  # Custom order number
    service_date = Column(DateTime, nullable=True)  # Service date
    next_service_date = Column(DateTime, nullable=True)  # Next service date
    certificate_number = Column(Text, nullable=True)  # Certificate number
    wire_roll_cert_number = Column(Text, nullable=True)  # Wire roll certificate number

    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"<WireSetCert(serial_number='{self.serial_number}', wire_set_group='{self.wire_set_group}', asset_id={self.asset_id})>"


class RefreshLog(Base):
    """Track history and results of Excel data refresh operations."""

    __tablename__ = "refresh_log"

    id = Column(Integer, primary_key=True)
    refreshed_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    # Store categories as JSON text for SQLite compatibility
    categories_updated = Column(Text, nullable=False)
    total_files_processed = Column(Integer, nullable=False)
    # Store details as JSON text for SQLite compatibility
    details = Column(Text, nullable=False)

    def set_categories_updated(self, categories):
        """Set categories_updated from a list."""
        self.categories_updated = json.dumps(categories)

    def get_categories_updated(self):
        """Get categories_updated as a list."""
        return json.loads(self.categories_updated) if self.categories_updated else []

    def set_details(self, details):
        """Set details from a dict."""
        self.details = json.dumps(details)

    def get_details(self):
        """Get details as a dict."""
        return json.loads(self.details) if self.details else {}

    def __repr__(self):
        return f"<RefreshLog(id={self.id}, refreshed_at='{self.refreshed_at}', categories={self.get_categories_updated()})>"
