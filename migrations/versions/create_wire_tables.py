"""create wire offsets and wire set certs tables

Revision ID: create_wire_tables
Revises: 3728761a6895
Create Date: 2025-06-04 00:00:00.000000

TODO: This migration creates:
1. wire_offsets table (append-only for historical data)
2. wire_set_certs table (for caching WireSetCerts.xlsx data)
3. wire_offsets_current view (for getting latest data per wirelot/block)

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "create_wire_tables"
down_revision: Union[str, None] = "3728761a6895"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    
    # Create wire_offsets table (append-only)
    op.create_table(
        "wire_offsets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("wirelot", sa.Text(), nullable=False),
        sa.Column("block", sa.Text(), nullable=False),
        sa.Column("col1", sa.Numeric(), nullable=True),
        sa.Column("col2", sa.Numeric(), nullable=True),
        sa.Column("col3", sa.Numeric(), nullable=True),
        sa.Column("col4", sa.Numeric(), nullable=True),
        sa.Column("col5", sa.Numeric(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint("id"),
        # Note: No unique constraint since this is append-only
    )
    
    # Create indexes for performance
    op.create_index("ix_wire_offsets_wirelot", "wire_offsets", ["wirelot"])
    op.create_index("ix_wire_offsets_wirelot_block", "wire_offsets", ["wirelot", "block"])
    op.create_index("ix_wire_offsets_created_at", "wire_offsets", ["created_at"])
    
    # Create wire_set_certs table
    op.create_table(
        "wire_set_certs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("serial_number", sa.Text(), nullable=False),
        sa.Column("wire_set_group", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("serial_number", name="uq_wire_set_certs_serial_number"),
    )
    
    # Create indexes for wire_set_certs
    op.create_index("ix_wire_set_certs_serial_number", "wire_set_certs", ["serial_number"])
    op.create_index("ix_wire_set_certs_wire_set_group", "wire_set_certs", ["wire_set_group"])
    
    # TODO: Create wire_offsets_current view
    # This view should return the latest record for each wirelot/block combination
    create_wire_offsets_current_view = """
    CREATE VIEW wire_offsets_current AS
    SELECT DISTINCT ON (wirelot, block)
        id,
        wirelot,
        block,
        col1,
        col2,
        col3,
        col4,
        col5,
        created_at
    FROM wire_offsets
    ORDER BY wirelot, block, created_at DESC;
    """
    
    op.execute(create_wire_offsets_current_view)


def downgrade() -> None:
    """Downgrade schema."""
    
    # Drop the view first
    op.execute("DROP VIEW IF EXISTS wire_offsets_current;")
    
    # Drop indexes
    op.drop_index("ix_wire_set_certs_wire_set_group", "wire_set_certs")
    op.drop_index("ix_wire_set_certs_serial_number", "wire_set_certs")
    op.drop_index("ix_wire_offsets_created_at", "wire_offsets")
    op.drop_index("ix_wire_offsets_wirelot_block", "wire_offsets")
    op.drop_index("ix_wire_offsets_wirelot", "wire_offsets")
    
    # Drop tables
    op.drop_table("wire_set_certs")
    op.drop_table("wire_offsets")
