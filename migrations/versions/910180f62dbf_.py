"""empty message

Revision ID: 910180f62dbf
Revises: 611d3a092e13
Create Date: 2021-11-28 20:51:48.920189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '910180f62dbf'
down_revision = '611d3a092e13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conference', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('conference', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('conference', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('talk', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('talk', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('talk', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('talk', 'deleted_at')
    op.drop_column('talk', 'updated_at')
    op.drop_column('talk', 'created_at')
    op.drop_column('conference', 'deleted_at')
    op.drop_column('conference', 'updated_at')
    op.drop_column('conference', 'created_at')
    # ### end Alembic commands ###