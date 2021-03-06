"""empty message

Revision ID: 232b13d4e86a
Revises: 14e31b3a860b
Create Date: 2019-06-17 02:51:42.186307

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '232b13d4e86a'
down_revision = '14e31b3a860b'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('google_recaptcha_secret', sa.String(), nullable=True))
    op.add_column('settings', sa.Column('google_recaptcha_site', sa.String(), nullable=True))
    op.add_column('settings', sa.Column('is_google_recaptcha_enabled', sa.Boolean(), server_default='False', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'is_google_recaptcha_enabled')
    op.drop_column('settings', 'google_recaptcha_site')
    op.drop_column('settings', 'google_recaptcha_secret')
    # ### end Alembic commands ###
