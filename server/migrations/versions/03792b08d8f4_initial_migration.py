"""Initial migration.

Revision ID: 03792b08d8f4
Revises: 
Create Date: 2024-06-26 13:21:08.633814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03792b08d8f4'
down_revision = None
branch_labels = None
depends_on = None


# def upgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.create_table('employees',
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('name', sa.String(), nullable=False),
#     sa.Column('salary', sa.Integer(), nullable=True),
#     sa.PrimaryKeyConstraint('id')
#     )
#     # ### end Alembic commands ###


# def downgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.drop_table('employees')
#     # ### end Alembic commands ###


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###