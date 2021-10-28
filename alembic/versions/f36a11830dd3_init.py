"""init

Revision ID: f36a11830dd3
Revises: 1a72ce576bd3
Create Date: 2021-10-27 16:17:21.032247

"""
from alembic import op
import sqlalchemy as sa
from db.models.patient import genderenum

# revision identifiers, used by Alembic.
revision = 'f36a11830dd3'
down_revision = '1a72ce576bd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
                    sa.Column('patient_id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('gender', sa.Enum(genderenum, name="gender"), nullable=False),
                    sa.Column('date_of_birth', sa.Date(), nullable=False),
                    sa.Column('age', sa.Integer(), nullable=False),
                    sa.Column('address', sa.String(), nullable=False),
                    sa.Column('contact_details', sa.String(), nullable=False),
                    sa.Column('blood_group', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('patient_id')
                    )
    op.create_index(op.f('ix_patient_patient_id'),
                    'patient', ['patient_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_patient_patient_id'), table_name='patient')
    op.drop_table('patient')
    # ### end Alembic commands ###
