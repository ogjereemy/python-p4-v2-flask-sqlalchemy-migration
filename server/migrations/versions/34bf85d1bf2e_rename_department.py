"""rename department

Revision ID: 34bf85d1bf2e
Revises: 3a9f841d754f
Create Date: 2024-06-26 13:33:17.107714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34bf85d1bf2e'
down_revision = '3a9f841d754f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###