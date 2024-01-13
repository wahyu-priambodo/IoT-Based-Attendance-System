"""modify 'user_rfid_hash' column

Revision ID: 97a5116b3148
Revises: 5501201e5e8c
Create Date: 2024-01-13 11:25:42.434950

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '97a5116b3148'
down_revision = '5501201e5e8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('user_rfid_hash',
               existing_type=mysql.VARCHAR(length=256),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('user_rfid_hash',
               existing_type=mysql.VARCHAR(length=256),
               nullable=False)

    # ### end Alembic commands ###