


from unittest.mock import Base
import uuid
from sqlalchemy import Column, String, Boolean

class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(
        uuid.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.UUID4,
        unique=True,
        nullable=False
    )