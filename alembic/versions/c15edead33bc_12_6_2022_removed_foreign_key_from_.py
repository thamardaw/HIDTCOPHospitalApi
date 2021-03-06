"""12_6_2022_removed_foreign_key_from_pharmacy_and_inventory_item

Revision ID: c15edead33bc
Revises: 1c5d98de9fb4
Create Date: 2022-06-12 10:19:06.194634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c15edead33bc'
down_revision = '1c5d98de9fb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('inventoryitem', 'sales_service_item_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_inventoryitem_sales_service_item_id'), 'inventoryitem', ['sales_service_item_id'], unique=False)
    op.drop_constraint('inventoryitem_sales_service_item_id_fkey', 'inventoryitem', type_='foreignkey')
    op.alter_column('pharmacyitem', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_pharmacyitem_category_id'), 'pharmacyitem', ['category_id'], unique=False)
    op.drop_constraint('pharmacyitem_category_id_fkey', 'pharmacyitem', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('pharmacyitem_category_id_fkey', 'pharmacyitem', 'category', ['category_id'], ['id'])
    op.drop_index(op.f('ix_pharmacyitem_category_id'), table_name='pharmacyitem')
    op.alter_column('pharmacyitem', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key('inventoryitem_sales_service_item_id_fkey', 'inventoryitem', 'salesserviceitem', ['sales_service_item_id'], ['id'])
    op.drop_index(op.f('ix_inventoryitem_sales_service_item_id'), table_name='inventoryitem')
    op.alter_column('inventoryitem', 'sales_service_item_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
