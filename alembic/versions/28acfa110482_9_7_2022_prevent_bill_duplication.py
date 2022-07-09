"""9_7_2022_prevent_bill_duplication

Revision ID: 28acfa110482
Revises: 664d6e199417
Create Date: 2022-07-09 21:26:50.583396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28acfa110482'
down_revision = '664d6e199417'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'payment', ['bill_id'])
    op.alter_column(
        table_name="patient",
        column_name="age",
        type_=sa.String(),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'payment', type_='unique')
    op.alter_column(
        table_name="patient",
        column_name="age",
        type_=sa.Integer(),
    )
    # ### end Alembic commands ###