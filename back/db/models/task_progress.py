import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, Boolean, Column, Uuid, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base_class import Base

class TaskProgress(Base):
    id: Mapped[str] = mapped_column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)3
    progress =  Column(Float(asdecimal=True), nullable=False, default = 0.0)        
    updated_at = Column(DateTime, default=datetime.now)
    user_id =  Column(Uuid(as_uuid=True),ForeignKey("user.id"))
    user = relationship("User",backref="task_assignments")  
    task_assignments_id =  Column(Uuid(as_uuid=True),ForeignKey("task.id"))
    task_assignments = relationship("Task_Assignments",backref="task_assignments")