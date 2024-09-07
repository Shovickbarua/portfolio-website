"""first migrations

Revision ID: b4fed5ab209f
Revises: 38e8170d7e4e
Create Date: 2024-09-07 16:45:26.145677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4fed5ab209f'
down_revision: Union[str, None] = '38e8170d7e4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
