"""First Revision

Revision ID: 66746fe8a190
Revises: 
Create Date: 2021-02-06 10:09:28.564007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66746fe8a190'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client_application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('application_base_url', sa.String(), nullable=False),
    sa.Column('application_public_key', sa.String(), nullable=False),
    sa.Column('server_public_key', sa.String(), nullable=False),
    sa.Column('server_private_key', sa.String(), nullable=False),
    sa.Column('css_url', sa.String(), nullable=True),
    sa.Column('client_token', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('is_account_contact', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('email',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(), server_default='Default', nullable=True),
    sa.Column('emailaddress', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('keys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('private_key', sa.String(), nullable=True),
    sa.Column('public_key', sa.String(), nullable=True),
    sa.Column('keys_status', sa.Enum('ok', 'invalid', name='keys_status_enum'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('invalidated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('push_notification_certificate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(), nullable=True),
    sa.Column('apns_certificate_uri', sa.String(), nullable=True),
    sa.Column('use_apns_sandbox', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.Column('fcm_key', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service_provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logo_url', sa.String(), nullable=True),
    sa.Column('authentication_url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('authentication_url')
    )
    op.create_table('contact_email',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.Column('email_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['email_id'], ['email.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(), nullable=True),
    sa.Column('registration_status', sa.Enum('started', 'installed', 'inprogress', 'expired', 'invalid', 'completed', name='registration_status_enum'), nullable=True),
    sa.Column('device_id', sa.String(), nullable=True),
    sa.Column('secret', sa.String(), nullable=True),
    sa.Column('push_notification_token', sa.String(), nullable=True),
    sa.Column('app_version', sa.String(), nullable=True),
    sa.Column('keystore', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('service_credentials', sa.DateTime(), nullable=True),
    sa.Column('push_notification_certificate_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['push_notification_certificate_id'], ['push_notification_certificate.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('user_registration_status', sa.Enum('started', 'email_sent', 'email_verified', 'completed', 'admin_disable', 'user_disable', 'account_cancelled', 'expired', 'deleted', name='user_registration_status_enum'), nullable=True),
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.Column('is_primary', sa.Boolean(), nullable=True),
    sa.Column('idtoken', sa.String(), nullable=True),
    sa.Column('secret1', sa.String(), nullable=True),
    sa.Column('secret2', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('authentication',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('auth_request_id', sa.String(), nullable=True),
    sa.Column('authentication_status', sa.Enum('started', 'notification_sent', 'identification_requested', 'validation_requested', 'completed', 'identification_started', 'identification_confirmed', name='authentication_status_enum'), nullable=True),
    sa.Column('authentication_result', sa.Enum('allowed', 'denied', 'failed', name='authentication_result_enum'), nullable=True),
    sa.Column('authentication_session_status', sa.Enum('active', 'inactive', 'expired', 'verifying', 'closed', 'idle', 'walkaway', name='authentication_session_status_enum'), nullable=True),
    sa.Column('authentication_method', sa.Enum('manual', 'bluetooth', 'geolocation', 'sonic', 'facial', 'validation_server', name='authentication_method_enum'), nullable=True),
    sa.Column('authentication_status_secret', sa.String(), nullable=True),
    sa.Column('app_version', sa.String(), nullable=True),
    sa.Column('devices', sa.String(), nullable=True),
    sa.Column('browser_device', sa.String(), nullable=True),
    sa.Column('mobile_device', sa.String(), nullable=True),
    sa.Column('desktop_device', sa.String(), nullable=True),
    sa.Column('browser', sa.String(), nullable=True),
    sa.Column('os', sa.String(), nullable=True),
    sa.Column('useragent', sa.String(), nullable=True),
    sa.Column('ipaddress', sa.String(), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('geolocation', sa.String(), nullable=True),
    sa.Column('ble_mobile', sa.String(), nullable=True),
    sa.Column('ble_desktop', sa.String(), nullable=True),
    sa.Column('walkaway_data', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('push_notification_certificate_id', sa.Integer(), nullable=True),
    sa.Column('logged_in_at', sa.DateTime(), nullable=True),
    sa.Column('logged_out_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['push_notification_certificate_id'], ['push_notification_certificate.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token_status', sa.Enum('new', 'inuse', 'expired', 'deleted', name='token_status_enum'), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('user_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('key', sa.String(), nullable=True),
    sa.Column('value', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_tag')
    op.drop_table('token')
    op.drop_table('authentication')
    op.drop_table('user')
    op.drop_table('device')
    op.drop_table('contact_email')
    op.drop_table('service_provider')
    op.drop_table('push_notification_certificate')
    op.drop_table('keys')
    op.drop_table('email')
    op.drop_table('contact')
    op.drop_table('client_application')
    # ### end Alembic commands ###