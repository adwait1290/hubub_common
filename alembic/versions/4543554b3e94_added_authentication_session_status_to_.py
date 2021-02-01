"""added authentication_session_status to authentication along with authentication_status_secret

Revision ID: 4543554b3e94
Revises: d80751cafd61
Create Date: 2017-12-14 10:59:25.100060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4543554b3e94'
down_revision = 'd80751cafd61'
branch_labels = None
depends_on = None
#CREATE TYPE AUTHENTICATION_SESSION_STATUS_ENUM AS ENUM ('active', 'inactive', 'expired');


def upgrade():
    pass


def downgrade():
    pass
