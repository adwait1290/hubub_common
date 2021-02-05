from hubub_common.models import BaseModel


class Hub(BaseModel):
    __tablename__ = 'hub'
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    bane