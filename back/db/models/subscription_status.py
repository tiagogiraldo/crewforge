import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, Boolean, Column, Uuid, String, DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base_class import Base

class Subscription_Status(Base):
    id: Mapped[str] = mapped_column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    is_active: Mapped[bool] = mapped_column(Boolean())
    expiration_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    user_id: Mapped[str] = mapped_column(Uuid(as_uuid=True), ForeignKey("user.id"))
    user = relationship("User", backref="subscription_status", uselist=False)
