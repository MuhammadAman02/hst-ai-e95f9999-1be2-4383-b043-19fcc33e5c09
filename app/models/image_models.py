from pydantic import BaseModel
from typing import List, Optional

class SkinToneAnalysis(BaseModel):
    skin_tone: str
    recommended_colors: List[str]

class ImageUpload(BaseModel):
    file: bytes
    filename: str

class SkinToneModification(BaseModel):
    image_id: str
    new_skin_tone: str

class ColorRecommendation(BaseModel):
    color_name: str
    hex_code: str
    confidence: float

class AnalysisResult(BaseModel):
    image_id: str
    original_skin_tone: str
    recommended_colors: List[ColorRecommendation]
    modified_image_url: Optional[str] = None