"""empty message

Revision ID: 0896f9507919
Revises: 
Create Date: 2018-09-07 14:51:16.152906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0896f9507919'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produces',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('money', sa.Integer(), nullable=True),
    sa.Column('Info', sa.String(length=200), nullable=True),
    sa.Column('have', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('tel', sa.String(length=11), nullable=True),
    sa.Column('birth', sa.String(length=10), nullable=True),
    sa.Column('money', sa.Integer(), nullable=True),
    sa.Column('jifen', sa.Integer(), nullable=True),
    sa.Column('Role', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tel'),
    sa.UniqueConstraint('username')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('money',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('money', sa.Integer(), nullable=True),
    sa.Column('jifen', sa.Integer(), nullable=True),
    sa.Column('payfor', sa.String(length=100), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('money')
    op.drop_table('messages')
    op.drop_table('users')
    op.drop_table('produces')
    # ### end Alembic commands ###
