"""Added phone_numbe2

Revision ID: acdda439a6cf
Revises: 3b39c55e9537
Create Date: 2024-09-26 13:12:24.651209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'acdda439a6cf'
down_revision: Union[str, None] = '3b39c55e9537'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_numbers', sa.String(length=12), nullable=True))
    op.drop_column('users', 'phone_number')
    op.drop_constraint('vehiculos_ibfk_4', 'vehiculos', type_='foreignkey')
    op.create_foreign_key(None, 'vehiculos', 'Autos_models', ['modelo_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vehiculos', type_='foreignkey')
    op.create_foreign_key('vehiculos_ibfk_4', 'vehiculos', 'autos_models', ['modelo_id'], ['id'], ondelete='CASCADE')
    op.add_column('users', sa.Column('phone_number', mysql.VARCHAR(length=12), nullable=True))
    op.drop_column('users', 'phone_numbers')
    op.create_table('detalle_venta',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('cantidad', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('subtotal', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('vehiculo_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venta_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='detalle_venta_ibfk_1', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['vehiculo_id'], ['vehiculos.id'], name='detalle_venta_ibfk_2', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['venta_id'], ['venta.id'], name='detalle_venta_ibfk_3', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('autos_models',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('modelo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('detalle_compra',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('cantidad', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('subtotal', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('vehiculo_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('compra_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['compra_id'], ['compra.id'], name='detalle_compra_ibfk_1', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='detalle_compra_ibfk_2', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['vehiculo_id'], ['vehiculos.id'], name='detalle_compra_ibfk_3', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
