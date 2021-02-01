"""added authentication_status_secretpart 2

Revision ID: 1d66f55f8e51
Revises: 6c639fc35f80
Create Date: 2017-12-14 11:12:37.846012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d66f55f8e51'
down_revision = '6c639fc35f80'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('authentication', sa.Column('authentication_status_secret', sa.String(), nullable=True))
    pass


def downgrade():
    op.drop_column('authentication', 'authentication_status_secret')
    pass
