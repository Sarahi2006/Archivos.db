"""crear tablas universidad

Revision ID: ba2b18a9d265
Revises: 504461f4f23b
Create Date: 2024-11-13 21:17:22.134758

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba2b18a9d265'
down_revision: Union[str, None] = '504461f4f23b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
