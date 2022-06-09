"""9_6_2022_added_is_active_inventory_item

Revision ID: 1c5d98de9fb4
Revises: a0f77459f976
Create Date: 2022-06-09 23:12:04.664903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c5d98de9fb4'
down_revision = 'a0f77459f976'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventoryitem', sa.Column('is_active', sa.Boolean(), server_default='true', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inventoryitem', 'is_active')
    # ### end Alembic commands ###