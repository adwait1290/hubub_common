"""added authentication_session_status part2

Revision ID: 1fbad26467d4
Revises: 1d66f55f8e51
Create Date: 2017-12-14 11:47:48.737992

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

# revision identifiers, used by Alembic.
revision = '1fbad26467d4'
down_revision = '1d66f55f8e51'
branch_labels = None
depends_on = None

authentication_session_status_enum = ENUM('valid', 'invalid', 'expired', name='authentication_session_status_enum', create_type=False)
def upgrade():
    op.add_column('authentication', sa.Column('authentication_session_status', authentication_session_status_enum, nullable=True))
    pass


def downgrade():
    op.drop_column('authentication', 'authentication_session_status')
    pass
