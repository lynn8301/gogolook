"""Modify table

Revision ID: 1536cefc8b83
Revises: 58d4240025e4
Create Date: 2024-03-21 19:24:03.497298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1536cefc8b83'
down_revision = '58d4240025e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_index('ix_task_name')
        batch_op.create_index(batch_op.f('ix_task_name'), ['name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_task_name'))
        batch_op.create_index('ix_task_name', ['name'], unique=1)

    # ### end Alembic commands ###
