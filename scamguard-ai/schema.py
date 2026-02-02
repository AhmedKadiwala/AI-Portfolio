from pydantic import BaseModel, Field
from typing import Literal, List


class ScamDetectionResult(BaseModel):
    classification: Literal["Scam", "Not Scam", "Uncertain"]
    intent_type: List[str]
    reasoning: str