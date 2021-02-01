"""Added user_registration_status to the user Table

Revision ID: d979d825a835
Revises: 4735b5751171
Create Date: 2017-12-12 12:09:12.611758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd979d825a835'
down_revision = '4735b5751171'
branch_labels = None
depends_on = None

# CREATE TYPE USER_REGISTRATION_STATUS_ENUM AS ENUM ('started', 'email_sent', 'email_verified', 'completed', 'admin_disable', 'user_disable', 'account_cancelled', 'expired', 'deleted');


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_registration_status', sa.Enum('started', 'email_sent', 'email_verified', 'completed', 'admin_disable', 'user_disable', 'account_cancelled', 'expired', 'deleted', name='user_registration_status_enum'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_registration_status')
    # ### end Alembic commands ###