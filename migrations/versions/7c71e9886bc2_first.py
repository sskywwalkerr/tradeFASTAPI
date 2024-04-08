"""First

Revision ID: 7c71e9886bc2
Revises: 
Create Date: 2024-04-08 20:03:01.497684

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c71e9886bc2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.drop_column('user', 'is_activ')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_activ', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###
