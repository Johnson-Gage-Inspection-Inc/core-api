"""redesign wire_offsets table schema

Revision ID: ac8ed2ac0165
Revises: b4f65b3e844e
Create Date: 2025-06-05 05:39:20.327364

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ac8ed2ac0165"
down_revision: Union[str, None] = "b4f65b3e844e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Redesign wire_offsets table with proper schema for correction factors."""

    # Drop the existing view first
    op.execute("DROP VIEW IF EXISTS wire_offsets_current")

    # Drop the existing table with incorrect schema
    op.drop_table("wire_offsets")

    # Create new wire_offsets table with proper schema
    op.create_table(
        "wire_offsets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "traceability_no",
            sa.Text(),
            nullable=False,
            comment="Wire lot/roll identifier (e.g., 072513A)",
        ),
        sa.Column(
            "nominal_temp",
            sa.Numeric(precision=8, scale=2),
            nullable=False,
            comment="Temperature in Celsius",
        ),
        sa.Column(
            "correction_factor",
            sa.Numeric(precision=10, scale=6),
            nullable=False,
            comment="Wire correction factor",
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("now()"),
            comment="When this record was created",
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("now()"),
            comment="When this record was last updated",
        ),
        sa.Column(
            "updated_by",
            sa.Text(),
            nullable=True,
            comment="SharePoint user who last modified the source file",
        ),
        sa.PrimaryKeyConstraint("id"),
        # Ensure each combination is unique per version (append-only with timestamps)
        sa.Index(
            "ix_wire_offsets_traceability_temp", "traceability_no", "nominal_temp"
        ),
    )

    # Create view to show most recent correction factors for each wire lot + temperature
    op.execute(
        """
        CREATE VIEW wire_offsets_current AS
        SELECT DISTINCT ON (traceability_no, nominal_temp) 
            id,
            traceability_no,
            nominal_temp,
            correction_factor,
            created_at,
            updated_at,
            updated_by
        FROM wire_offsets
        ORDER BY traceability_no, nominal_temp, created_at DESC
    """
    )


def downgrade() -> None:
    """Restore old wire_offsets table schema."""

    # Drop the new view and table
    op.execute("DROP VIEW IF EXISTS wire_offsets_current")
    op.drop_table("wire_offsets")

    # Recreate the old table structure (for rollback compatibility)
    op.create_table(
        "wire_offsets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("wirelot", sa.Text(), nullable=False),
        sa.Column("block", sa.Text(), nullable=False),
        sa.Column("col1", sa.Numeric()),
        sa.Column("col2", sa.Numeric()),
        sa.Column("col3", sa.Numeric()),
        sa.Column("col4", sa.Numeric()),
        sa.Column("col5", sa.Numeric()),
        sa.Column(
            "created_at", sa.DateTime(), nullable=False, server_default=sa.text("now()")
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    # Recreate old view
    op.execute(
        """
        CREATE VIEW wire_offsets_current AS
        SELECT DISTINCT ON (wirelot, block) 
            id, wirelot, block, col1, col2, col3, col4, col5, created_at
        FROM wire_offsets
        ORDER BY wirelot, block, created_at DESC
    """
    )
