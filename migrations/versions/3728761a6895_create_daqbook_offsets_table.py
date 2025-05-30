"""create daqbook_offsets table

Revision ID: 3728761a6895
Revises: 
Create Date: 2025-05-30 16:49:52.297431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3728761a6895'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create daqbook_offsets table
    op.create_table(
        'daqbook_offsets',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('tn', sa.Text(), nullable=False),
        sa.Column('temp', sa.Numeric(), nullable=False),
        sa.Column('point', sa.Integer(), nullable=False),
        sa.Column('reading', sa.Numeric(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('tn', 'temp', 'point', name='uq_daqbook_offsets_tn_temp_point')
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Drop daqbook_offsets table
    op.drop_table('daqbook_offsets')
