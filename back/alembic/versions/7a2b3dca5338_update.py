"""update

Revision ID: 7a2b3dca5338
Revises: 1dbb8cbd79ae
Create Date: 2024-11-27 17:44:27.716973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a2b3dca5338'
down_revision: Union[str, None] = '1dbb8cbd79ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'project', 'user', ['owner_id'], ['id'])
    op.create_foreign_key(None, 'subscription', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'subscription_status', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'task_assignment', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'team_member', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'team_member', type_='foreignkey')
    op.drop_constraint(None, 'task_assignment', type_='foreignkey')
    op.drop_constraint(None, 'subscription_status', type_='foreignkey')
    op.drop_constraint(None, 'subscription', type_='foreignkey')
    op.drop_constraint(None, 'project', type_='foreignkey')
    # ### end Alembic commands ###