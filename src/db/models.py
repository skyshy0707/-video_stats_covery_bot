from sqlalchemy import (
    Column, 
    DateTime, 
    Float,
    ForeignKey,
    Integer,
    String,
    Uuid
)

from db.engine import Base


class Creator(Base):

    __tablename__ = "creator"

    id = Column(Uuid, primary_key=True)

class Video(Base):

    __tablename__ = "video"

    id = Column(Uuid, primary_key=True)
    creator_id = Column(Uuid, nullable=False)
    video_created_at = Column(DateTime(timezone=True), nullable=False)
    views_count = Column(Integer, default=0)
    likes_count = Column(Integer, default=0)
    comments_count = Column(Integer, default=0)
    reports_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)


class SnapShot(Base):

    __tablename__ = "snapshot"

    id = Column(Uuid, primary_key=True)
    video_id = Column(ForeignKey("video.id"), nullable=False)
    delta_views_count = Column(Integer, default=0)
    delta_likes_count = Column(Integer, default=0)
    delta_comments_count = Column(Integer, default=0)
    delta_reports_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)