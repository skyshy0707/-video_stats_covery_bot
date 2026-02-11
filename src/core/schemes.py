from typing import List

from pydantic import AliasChoices, AliasPath, BaseModel, Field, model_serializer

from common_types import datetime, UTC


class Object(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime

class SnapShot(Object):

    video_id: str
    delta_views_count: int = Field(default=0)
    delta_likes_count: int = Field(default=0)
    delta_comments_count: int = Field(default=0)
    delta_reports_count: int = Field(default=0)


class Video(Object):

    creator_id: str
    video_created_at: datetime
    views_count: int = Field(default=0)
    likes_count: int = Field(default=0)
    comments_count: int = Field(default=0)
    reports_count: int = Field(default=0)
    snapshots: List[SnapShot] = Field(exclude=True)