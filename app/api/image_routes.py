from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.models.image_models import SkinToneAnalysis, ImageUpload, SkinToneModification, AnalysisResult, ColorRecommendation
from app.services.image_service import ImageService
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

def get_image_service():
    return ImageService()

@router.post("/upload", response_model=AnalysisResult)
async def upload_image(file: UploadFile = File(...), image_service: ImageService = Depends(get_image_service)):
    try:
        contents = await file.read()
        image_id = image_service.save_image(contents, file.filename)
        skin_tone, recommended_colors = image_service.analyze_skin_tone(contents)
        
        color_recommendations = [
            ColorRecommendation(color_name=color, hex_code="#000000", confidence=0.8)
            for color in recommended_colors
        ]
        
        return AnalysisResult(
            image_id=image_id,
            original_skin_tone=skin_tone,
            recommended_colors=color_recommendations,
            modified_image_url=f"/static/uploads/{image_id}{file.filename[-4:]}"
        )
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing image")

@router.post("/modify-skin-tone", response_model=AnalysisResult)
async def modify_skin_tone(modification: SkinToneModification, image_service: ImageService = Depends(get_image_service)):
    try:
        modified_image_url = image_service.modify_skin_tone(modification.image_id, modification.new_skin_tone)
        
        # Re-analyze the modified image (in a real application, you'd analyze the actual modified image)
        _, recommended_colors = image_service.analyze_skin_tone(b'')  # Placeholder
        
        color_recommendations = [
            ColorRecommendation(color_name=color, hex_code="#000000", confidence=0.8)
            for color in recommended_colors
        ]
        
        return AnalysisResult(
            image_id=modification.image_id,
            original_skin_tone=modification.new_skin_tone,
            recommended_colors=color_recommendations,
            modified_image_url=modified_image_url
        )
    except Exception as e:
        logger.error(f"Error modifying skin tone: {str(e)}")
        raise HTTPException(status_code=500, detail="Error modifying skin tone")