"""empty message

Revision ID: 53093c7a4501
Revises: 46c1419fe4bc
Create Date: 2019-01-21 21:47:26.746059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53093c7a4501'
down_revision = '46c1419fe4bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    # ### end Alembic commands ###
