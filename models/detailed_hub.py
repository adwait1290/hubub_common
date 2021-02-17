from enum import Enum

<<<<<<< HEAD
from marshmallow import post_load, fields
from marshmallow_sqlalchemy import ModelSchema

from .base import BaseModel
from .db import Session
=======
from marshmallow import post_load

from .base import BaseModel, ModelSchema, fields
from .db import Session
from .user_device import *
>>>>>>> ed15ccc59283ddd4edaa2b4c490b126cb9c98aa6
from ._types import DeviceType, RegistrationStatus


import sqlalchemy as sa


class DetailedHub(BaseModel):
    __tablename__ = 'SimpleHub'
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    title = sa.Column(sa.String, nullable=True)
    is_published = sa.Column(sa.Boolean, default=false)
    hub_url = sa.Column(sa.String, nullable=True)
    image_url = sa.Column(sa.String, nullable=True)
    order = sa.Column(sa.Integer, default=0)
    created_at = sa.Column(sa.DateTime, server_default=func.now())
    updated_at = sa.Column(sa.DateTime, server_default=func.now())
    deleted_at = sa.Column(sa.DateTime, nullable=True, server_default=None)

    @post_load
    def make_detailed_hub(self, data):
        return DetailedHub(**data)


class DetailedHubSchema(ModelSchema):
    id = fields.Integer(required=False)
    title = fields.String(required=False)
    is_published = fields.Boolean(required=True)
    hub_url = fields.String(required=False)
    image_url = fields.String(required=False)
    order = fields.Integer(required=True)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
    deleted_at = fields.DateTime(required=False)

    class Meta:
        model = DetailedHub
        sqla_session = Session
        strict = False