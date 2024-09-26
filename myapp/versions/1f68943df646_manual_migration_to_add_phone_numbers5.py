"""Manual migration to add phone_numbers5

Revision ID: 1f68943df646
Revises: 3f913f2de149
Create Date: 2024-09-26 13:17:26.517725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f68943df646'
down_revision: Union[str, None] = '3f913f2de149'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(length=12)))
    pass


def downgrade() -> None:
    op.drop_column('users', 'phone_numbers')
    pass
