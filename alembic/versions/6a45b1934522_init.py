"""init

Revision ID: 6a45b1934522
Revises: a0d21a780cff
Create Date: 2021-11-01 21:35:45.043751

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6a45b1934522'
down_revision = 'a0d21a780cff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_basemodel_id', table_name='basemodel')
    op.drop_table('basemodel')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('basemodel',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_time', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('updated_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('created_user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('updated_user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['created_user_id'], ['user.id'], name='basemodel_created_user_id_fkey'),
    sa.ForeignKeyConstraint(['updated_user_id'], ['user.id'], name='basemodel_updated_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='basemodel_pkey')
    )
    op.create_index('ix_basemodel_id', 'basemodel', ['id'], unique=False)
    # ### end Alembic commands ###
