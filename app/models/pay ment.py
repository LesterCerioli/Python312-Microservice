

from email.mime import base
from enum import Enum
from uuid import UUID
import uuid
from sqlalchemy import Column, String, Table, ForeignKey

class PaymentInterval(Enum):
    MONTHLY = 'monthly'
    YEARLY = 'yearly'
class Payment(base):
    __tablename__ = 'payments'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False
    )
    subscription_id = Column(UUID(as_uuid=True), ForeignKey('subscriptions.id'), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    interval = Column(SQLEnum(PaymentInterval), nullable=False)
    payment_date = Column(DateTime(timezone=True), server_default=func.now())
    transaction_id = Column(String(100), unique=True)

    subscription = relationship("Subscription", back_populates="payments")

    def __repr__(self):
        return f"<Payment(amount={self.amount}, interval={self.interval.value})>"