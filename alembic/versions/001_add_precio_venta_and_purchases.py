"""add precio_venta and purchases tables

Revision ID: 001
Revises: 
Create Date: 2026-03-21

"""
from alembic import op
import sqlalchemy as sa

revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Agregar precio_venta a products (si no existe)
    op.execute("""
        ALTER TABLE products ADD COLUMN IF NOT EXISTS precio_venta FLOAT;
    """)

    # Crear tabla purchases (si no existe)
    op.execute("""
        CREATE TABLE IF NOT EXISTS purchases (
            id SERIAL PRIMARY KEY,
            precio_total FLOAT NOT NULL,
            fecha TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );
    """)

    # Crear tabla purchase_items (si no existe)
    op.execute("""
        CREATE TABLE IF NOT EXISTS purchase_items (
            id SERIAL PRIMARY KEY,
            purchase_id INTEGER REFERENCES purchases(id),
            product_id INTEGER REFERENCES products(id),
            quantity INTEGER NOT NULL
        );
    """)


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS purchase_items;")
    op.execute("DROP TABLE IF EXISTS purchases;")
    op.execute("ALTER TABLE products DROP COLUMN IF EXISTS precio_venta;")
