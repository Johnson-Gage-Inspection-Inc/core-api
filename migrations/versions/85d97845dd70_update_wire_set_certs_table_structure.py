"""update_wire_set_certs_table_structure

Revision ID: 85d97845dd70
Revises: create_wire_tables
Create Date: 2025-06-05 02:08:11.373994

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "85d97845dd70"
down_revision: Union[str, None] = "create_wire_tables"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add missing columns to wire_set_certs table to match Excel schema."""
    # Add all missing columns from WireSetCerts.xlsx
    op.add_column("wire_set_certs", sa.Column("asset_id", sa.Integer(), nullable=True))
    op.add_column("wire_set_certs", sa.Column("asset_tag", sa.Text(), nullable=True))
    op.add_column(
        "wire_set_certs", sa.Column("custom_order_number", sa.Text(), nullable=True)
    )
    op.add_column(
        "wire_set_certs", sa.Column("service_date", sa.DateTime(), nullable=True)
    )
    op.add_column(
        "wire_set_certs", sa.Column("next_service_date", sa.DateTime(), nullable=True)
    )
    op.add_column(
        "wire_set_certs", sa.Column("certificate_number", sa.Text(), nullable=True)
    )
    op.add_column(
        "wire_set_certs", sa.Column("wire_roll_cert_number", sa.Text(), nullable=True)
    )


def downgrade() -> None:
    """Remove the added columns."""
    op.drop_column("wire_set_certs", "wire_roll_cert_number")
    op.drop_column("wire_set_certs", "certificate_number")
    op.drop_column("wire_set_certs", "next_service_date")
    op.drop_column("wire_set_certs", "service_date")
    op.drop_column("wire_set_certs", "custom_order_number")
    op.drop_column("wire_set_certs", "asset_tag")
    op.drop_column("wire_set_certs", "asset_id")
