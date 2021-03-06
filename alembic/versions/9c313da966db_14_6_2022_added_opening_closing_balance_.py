"""14_6_2022_added_opening_closing_balance_inventory_transaction

Revision ID: 9c313da966db
Revises: 305a48b1c9b4
Create Date: 2022-06-14 20:10:34.852068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c313da966db'
down_revision = '305a48b1c9b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventorytransaction', sa.Column('opening_balance', sa.Integer(), nullable=False))
    op.add_column('inventorytransaction', sa.Column('closing_balance', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inventorytransaction', 'closing_balance')
    op.drop_column('inventorytransaction', 'opening_balance')
    # ### end Alembic commands ###
