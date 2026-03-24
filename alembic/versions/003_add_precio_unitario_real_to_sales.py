"""add precio_unitario_real to sales

Revision ID: 003
Revises: 002_add_discounts
Create Date: 2024-01-01 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

revision = '003'
down_revision = '002_add_discounts'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('sales', sa.Column('precio_unitario_real', sa.Float(), nullable=True))


def downgrade():
    op.drop_column('sales', 'precio_unitario_real')