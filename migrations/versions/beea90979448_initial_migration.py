"""Initial Migration

Revision ID: beea90979448
Revises: fe152bb9581f
Create Date: 2019-08-12 08:54:55.843884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beea90979448'
down_revision = 'fe152bb9581f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'profile_pic_path')
    # ### end Alembic commands ###