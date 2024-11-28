import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, Boolean, Column, Uuid, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base_class import Base


class Task(Base):
    id: Mapped[str] = mapped_column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True, index=True)
    status = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    project_id =  Column(Uuid(as_uuid=True),ForeignKey("project.id"))
    project = relationship("Project",backref="tasks")
    # task_assignments = relationship("Task_Assignment",back_populates="task")
