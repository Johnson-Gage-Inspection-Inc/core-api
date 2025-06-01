# db/models.py
from sqlalchemy import Column, Integer, Text, Numeric, UniqueConstraint
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
        UniqueConstraint('tn', 'temp', 'point', name='uq_daqbook_offsets_tn_temp_point'),
    )

    @property
    def delta(self):
        """Calculate delta as (reading - temp) * -1, rounded to 2 decimal places."""
        return round((float(self.reading) - float(self.temp)) * -1, 2)

    def __repr__(self):
        return f"<DaqbookOffset(tn='{self.tn}', temp={self.temp}, point={self.point}, reading={self.reading})>"
