"""renamed 'massage' to 'message' in models.py

Revision ID: 1b33dccacc24
Revises: 193c1aa89141
Create Date: 2023-11-21 19:16:22.107779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b33dccacc24'
down_revision = '193c1aa89141'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('message', sa.String(length=256), nullable=True))
        batch_op.drop_column('massage')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('massage', sa.VARCHAR(length=256), nullable=True))
        batch_op.drop_column('message')

    # ### end Alembic commands ###
