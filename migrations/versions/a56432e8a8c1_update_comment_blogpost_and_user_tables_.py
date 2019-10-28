"""Update comment, blogpost and user tables and db relationships

Revision ID: a56432e8a8c1
Revises: 1724ad709e28
Create Date: 2019-10-28 15:36:33.015740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a56432e8a8c1'
down_revision = '1724ad709e28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blogpost', sa.String(length=700), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('blogpost_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blogpost_id'], ['blogposts.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    op.drop_table('comments')
    op.drop_table('blogposts')
    # ### end Alembic commands ###
