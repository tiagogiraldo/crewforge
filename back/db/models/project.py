import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, Boolean, Column, Uuid, String, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base_class import Base


class Project(Base):
    id: Mapped[str] = mapped_column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True, index=True)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    owner_id =  Column(Uuid(as_uuid=True),ForeignKey("user.id"))