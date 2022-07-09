from pydantic import BaseModel

from app.core.enums import CommentType


class CommentTypePredictionResult(BaseModel):
    label: CommentType
    score: float
    elapsed_time: float
