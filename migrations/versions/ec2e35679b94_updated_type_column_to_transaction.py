"""updated type column to Transaction

Revision ID: ec2e35679b94
Revises: c0aca3cf2c07
Create Date: 2023-06-20 13:40:46.686285

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ec2e35679b94'
down_revision = 'c0aca3cf2c07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.alter_column('type',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.String(length=25),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.alter_column('type',
               existing_type=sa.String(length=25),
               type_=mysql.VARCHAR(length=10),
               existing_nullable=True)

    # ### end Alembic commands ###