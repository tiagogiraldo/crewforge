"""create table migrations

Revision ID: e4101eb49156
Revises: f2e3179c00bc
Create Date: 2024-11-26 23:16:44.013990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e4101eb49156'
down_revision: Union[str, None] = 'f2e3179c00bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_payment_id', table_name='payment')
    op.drop_table('payment')
    op.add_column('subscription', sa.Column('payment', sa.Numeric(precision=5, scale=2), nullable=False))
    op.drop_index('ix_subscription_name', table_name='subscription')
    op.drop_column('subscription', 'is_active')
    op.drop_column('subscription', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscription', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('subscription', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.create_index('ix_subscription_name', 'subscription', ['name'], unique=True)
    op.drop_column('subscription', 'payment')
    op.create_table('payment',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('amount', sa.NUMERIC(precision=5, scale=2), autoincrement=False, nullable=False),
    sa.Column('payment_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('subscription_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['subscription_id'], ['subscription.id'], name='payment_subscription_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='payment_pkey')
    )
    op.create_index('ix_payment_id', 'payment', ['id'], unique=False)
    # ### end Alembic commands ###
