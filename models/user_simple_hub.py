<<<<<<< HEAD
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from .base import BaseModel
=======
from .base import BaseModel, ModelSchema, fields
>>>>>>> ed15ccc59283ddd4edaa2b4c490b126cb9c98aa6

from .db import Session

import sqlalchemy as sa


class UserSimpleHub(BaseModel):
    __tablename__ = 'user_simple_hub'
    one_to_many = True
    user_id = sa.Column(sa.ForeignKey('user_id', ondelete='CASCADE'),
                        unique=False)
    detailed_hub_id = sa.Column(sa.ForeignKey('simple_hub_id', ondelete='CASCADE'),
                                unique=False)


class UserSimpleHubScema(ModelSchema):
    id = fields.Integer(required=False)
    user_id = fields.Integer(required=True)
    user_detailed_hub_id = fields.Integer(required=True)

    class Meta:
        model = UserSimpleHub
        sqla_session = Session
        strict = False