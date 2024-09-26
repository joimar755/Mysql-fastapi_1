"""Manual migration to add phone_numbers8

Revision ID: ab7e9f1ca4ca
Revises: 1f68943df646
Create Date: 2024-09-26 13:18:34.225002

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab7e9f1ca4ca'
down_revision: Union[str, None] = '1f68943df646'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('users', 'phone_numbers')
    pass


def downgrade() -> None:
    pass
