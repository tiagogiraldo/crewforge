import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, Boolean, Column, Uuid, String, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base_class import Base


class Team_Member(Base):
    id: Mapped[str] = mapped_column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    role = Column(String, nullable=False, index=True)
    user_id =  Column(Uuid(as_uuid=True),ForeignKey("user.id"))
    user = relationship("User",backref="team_members")   
    team_id =  Column(Uuid(as_uuid=True),ForeignKey("team.id"))
    team = relationship("Team",backref="team_members")
