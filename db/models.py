# db/models.py
from sqlalchemy import Column, Integer, Numeric, Text, UniqueConstraint, DateTime, func
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
    Append-only table for wire offset data.
    
    TODO: This table stores historical wire offset measurements.
    Each record represents a single measurement event with timestamp.
    Use wire_offsets_current view for latest data per wirelot/block.
    """
    __tablename__ = "wire_offsets"

    id = Column(Integer, primary_key=True)
    wirelot = Column(Text, nullable=False)  # e.g. "123456A"
    block = Column(Text, nullable=False)  # "Top" or "Bottom"
    col1 = Column(Numeric, nullable=True)
    col2 = Column(Numeric, nullable=True)
    col3 = Column(Numeric, nullable=True)
    col4 = Column(Numeric, nullable=True)
    col5 = Column(Numeric, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    # TODO: Add source tracking fields like source_file, imported_by, etc.

    def __repr__(self):
        return f"<WireOffset(id={self.id}, wirelot='{self.wirelot}', block='{self.block}', created_at={self.created_at})>"


class WireSetCert(Base):
    """
    Cached data from WireSetCerts.xlsx for mapping serial numbers to wire sets.
    
    TODO: This table caches the WireSetCerts.xlsx data from SharePoint.
    It maps individual wire serial numbers (like 'J201') to their wire set groups.
    Should be refreshed periodically or on-demand via API.
    """
    __tablename__ = "wire_set_certs"

    id = Column(Integer, primary_key=True)
    serial_number = Column(Text, nullable=False, unique=True)  # e.g. "J201"
    wire_set_group = Column(Text, nullable=False)  # e.g. "J201-J214" 
    # TODO: Add additional fields from WireSetCerts.xlsx as needed
    # cert_date = Column(Date, nullable=True)
    # cert_status = Column(Text, nullable=True)
    # notes = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<WireSetCert(serial_number='{self.serial_number}', wire_set_group='{self.wire_set_group}')>"
