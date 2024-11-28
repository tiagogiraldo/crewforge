import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, Boolean, Column, Uuid, String, DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base_class import Base



class Subscription(Base):
    id: Mapped[str] = mapped_column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    subscription_type = Column(String, nullable=False, index=True)
    payment: Mapped[float] = mapped_column(Numeric(precision=7, scale=2), nullable=False, default=0)
    payment_date = Column(DateTime, default=datetime.now, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    user_id =  Column(Uuid(as_uuid=True),ForeignKey("user.id"))
    user = relationship("User",backref="subscriptions")