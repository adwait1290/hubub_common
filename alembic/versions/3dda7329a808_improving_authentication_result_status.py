"""improving authentication result status

Revision ID: 3dda7329a808
Revises: 4668aeb9cddd
Create Date: 2017-12-11 17:41:01.336031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dda7329a808'
down_revision = '4668aeb9cddd'
branch_labels = None
depends_on = None

# DROP TYPE AUTHENTICATION_RESULT_ENUM;
# CREATE TYPE AUTHENTICATION_RESULT_ENUM AS ENUM ('allowed', 'denied', 'failed');


# AUTHENTICATION_RESULT_ENUM = ENUM('allowed', 'denied', 'failed', name='AUTHENTICATION_RESULT_ENUM', create_type=False)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    pass
    # op.alter_column('authentication', 'authentication_result',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.Enum('allowed', 'denied', 'failed', name='authentication_result_enum'),
    #            existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass

    # op.alter_column('authentication', 'authentication_result',
    #            existing_type=sa.Enum('allowed', 'denied', 'failed', name='authentication_result_enum'),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # ### end Alembic commands ###