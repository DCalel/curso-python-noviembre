"""add genero column to alumnos table

Revision ID: 96cd02ed84ac
Revises: 79e6c3f298bc
Create Date: 2023-01-04 22:50:03.585911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96cd02ed84ac'
down_revision = '79e6c3f298bc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("alumnos",
        sa.Column("genero", sa.String())
    )


def downgrade() -> None:
    op.drop_column("alumnos","genero")
