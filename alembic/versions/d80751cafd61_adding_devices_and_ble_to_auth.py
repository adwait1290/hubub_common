"""adding devices and ble to auth

Revision ID: d80751cafd61
Revises: d979d825a835
Create Date: 2017-12-12 16:10:02.188520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd80751cafd61'
down_revision = 'd979d825a835'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authentication', sa.Column('ble_desktop', sa.String(), nullable=True))
    op.add_column('authentication', sa.Column('ble_mobile', sa.String(), nullable=True))
    op.add_column('authentication', sa.Column('browser_device', sa.String(), nullable=True))
    op.add_column('authentication', sa.Column('desktop_device', sa.String(), nullable=True))
    op.add_column('authentication', sa.Column('mobile_device', sa.String(), nullable=True))
    op.drop_column('authentication', 'device')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authentication', sa.Column('device', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('authentication', 'mobile_device')
    op.drop_column('authentication', 'desktop_device')
    op.drop_column('authentication', 'browser_device')
    op.drop_column('authentication', 'ble_mobile')
    op.drop_column('authentication', 'ble_desktop')
    # ### end Alembic commands ###
