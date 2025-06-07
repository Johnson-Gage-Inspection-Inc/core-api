"""add refresh_log table

Revision ID: b4f65b3e844e
Revises: 85d97845dd70
Create Date: 2025-06-05 05:09:17.421770

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b4f65b3e844e"
down_revision: Union[str, None] = "85d97845dd70"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create refresh_log table."""
    op.create_table(
        "refresh_log",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("refreshed_at", sa.DateTime(), nullable=False),
        sa.Column(
            "categories_updated", sa.Text(), nullable=False
        ),  # JSON serialized as Text for SQLite compatibility
        sa.Column("total_files_processed", sa.Integer(), nullable=False),
        sa.Column(
            "details", sa.Text(), nullable=True
        ),  # JSON serialized as Text for SQLite compatibility
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Drop refresh_log table."""
    op.drop_table("refresh_log")
