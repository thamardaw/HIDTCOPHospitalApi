"""14_6_2022_added_transaction_type_in_invtx

Revision ID: 497c7245f498
Revises: 9c313da966db
Create Date: 2022-06-14 23:53:01.554138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '497c7245f498'
down_revision = '9c313da966db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventorytransaction', sa.Column('transaction_type', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inventorytransaction', 'transaction_type')
    # ### end Alembic commands ###
