from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.dialects.postgresql import UUID  # Para PostgreSQL (ou use sqlalchemy.UUID para outros DBs)
from sqlalchemy.orm import relationship, declarative_base
import uuid

Base = declarative_base()  # Correção: Usar declarative_base do SQLAlchemy


podcast_category = Table(
    'podcast_category',
    Base.metadata,
    Column('podcast_id', UUID(as_uuid=True), ForeignKey('podcasts.id')),
    Column('category_id', UUID(as_uuid=True), ForeignKey('categories.id'))
)

class Podcast(Base):
    __tablename__ = 'podcasts'

    id = Column(
        UUID(as_uuid=True),  
        primary_key=True,
        default=uuid.uuid4,  
        unique=True,
        nullable=False
    )
    title = Column(String(100), nullable=False)
    author = Column(String(50))

    categories = relationship(
        "Category",  # Certifique-se de que a classe Category existe
        secondary=podcast_category,
        back_populates="podcasts"
    )

