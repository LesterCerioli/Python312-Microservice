from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID

from unittest.mock import Base
from uuid import UUID
import uuid


class Category(Base):
    __tablename__ = "categories"

    id = Column(
        UUID(as_uuid=True),  
        primary_key=True,
        default=uuid.uuid4,  
        unique=True,
        nullable=False,
        index=True
    )

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    slug = Column(String(100), unique=True, nullable=False)