"""Add Support Random User-Agent

Revision ID: 31f92220c0d0
Revises: 4f045f53bef8
Create Date: 2024-06-01 21:28:33.310627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31f92220c0d0'
down_revision = '4f045f53bef8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hosts', sa.Column('random_user_agent', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hosts', 'random_user_agent')
    # ### end Alembic commands ###
