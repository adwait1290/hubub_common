
from .base import BaseModel, ModelSchema, fields

from .db import Session

import sqlalchemy as sa
from sqlalchemy import (
        Index, DDL, event, FetchedValue, func, Column, false,
        Integer, ForeignKey, String, DateTime, UniqueConstraint, Boolean
    )

from sqlalchemy.orm import relationship


class UserTag(BaseModel):
    __tablename__ = 'user_tag'
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id', ondelete='CASCADE'))
    key = sa.Column('key', sa.String)
    value = sa.Column('value', sa.String)

class UserTagSchema(ModelSchema):
    key = fields.String(required=True)
    value = fields.String(required=False, missing=None)

    class Meta:
        model = UserTag
        sqla_session = Session
        strict = False