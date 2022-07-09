from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.models.payload import TextPayload
from app.models.prediction import CommentTypePredictionResult
from app.services.models import CommentTypeAnalysisModel

router = APIRouter()


@router.post("/predict", response_model=CommentTypePredictionResult, name="predict")
def post_predict(
    request: Request, data: TextPayload = None,
) -> CommentTypePredictionResult:

    model: CommentTypeAnalysisModel = request.app.state.model
    prediction: CommentTypePredictionResult = model.predict(data)

    return prediction
