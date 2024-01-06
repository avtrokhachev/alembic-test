"""create books table

Revision ID: c3f37d20be0f
Revises: 
Create Date: 2024-01-05 22:58:38.751095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3f37d20be0f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text),
    )


def downgrade() -> None:
    pass
