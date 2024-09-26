"""Manual migration to add phone_numbers

Revision ID: 3f913f2de149
Revises: acdda439a6cf
Create Date: 2024-09-26 13:15:10.580437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f913f2de149'
down_revision: Union[str, None] = 'acdda439a6cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(length=12)))
    pass


def downgrade() -> None:
    op.drop_column('users', 'phone_numbers')
    pass
