"""update

Revision ID: 1dbb8cbd79ae
Revises: 506dc7585f05
Create Date: 2024-11-27 17:24:17.995442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1dbb8cbd79ae'
down_revision: Union[str, None] = '506dc7585f05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_subscription_status_id', table_name='subscription_status')
    op.drop_table('subscription_status')
    op.create_foreign_key(None, 'project', 'user', ['owner_id'], ['id'])
    op.create_foreign_key(None, 'subscription', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'task_assignment', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'team_member', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'team_member', type_='foreignkey')
    op.drop_constraint(None, 'task_assignment', type_='foreignkey')
    op.drop_constraint(None, 'subscription', type_='foreignkey')
    op.drop_constraint(None, 'project', type_='foreignkey')
    op.create_table('subscription_status',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('expiration_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='subscription_status_pkey')
    )
    op.create_index('ix_subscription_status_id', 'subscription_status', ['id'], unique=False)
    # ### end Alembic commands ###