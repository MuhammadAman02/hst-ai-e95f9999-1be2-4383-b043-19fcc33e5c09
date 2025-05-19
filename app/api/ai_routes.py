from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
import logging

from app.models.ai_models import (
    Message, Conversation,
    TextAnalysisRequest, TextAnalysisResponse,
    RecommendationRequest, RecommendationResponse,
    Transaction, FraudDetectionResult
)
from app.services.ai_services import (
    LLMService, TextAnalysisService,
    RecommendationService, FraudDetectionService
)

# Configure logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

# Service dependencies
def get_llm_service():
    """Dependency for LLM service."""
    return LLMService(model_name="gpt-3.5-turbo")

def get_text_analysis_service():
    """Dependency for text analysis service."""
    return TextAnalysisService(model_name="bert-base-uncased")

def get_recommendation_service():
    """Dependency for recommendation service."""
    return RecommendationService(model_name="recommendation-model")

def get_fraud_detection_service():
    """Dependency for fraud detection service."""
    return FraudDetectionService(model_name="fraud-detection-model")

# Chatbot endpoints
@router.post("/chat", response_model=dict)
async def chat(message: str, conversation_id: Optional[str] = None, llm_service: LLMService = Depends(get_llm_service)):
    """Chat endpoint for conversational AI."""
    try:
        # In a real implementation, you would retrieve the conversation from a database
        # For simplicity, we're just creating a new message and generating a response
        user_message = {"role": "user", "content": message}
        response = await llm_service.generate_response([user_message])
        
        return {
            "response": response,
            "conversation_id": conversation_id or "new_conversation"
        }
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Text Analysis endpoints
@router.post("/analyze", response_model=TextAnalysisResponse)
async def analyze_text(
    request: TextAnalysisRequest,
    text_analysis_service: TextAnalysisService = Depends(get_text_analysis_service)
):
    """Analyze text using NLP models."""
    try:
        return await text_analysis_service.analyze_text(request)
    except Exception as e:
        logger.error(f"Error in text analysis endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Recommendation endpoints
@router.post("/recommend", response_model=RecommendationResponse)
async def get_recommendations(
    request: RecommendationRequest,
    recommendation_service: RecommendationService = Depends(get_recommendation_service)
):
    """Get recommendations for a user."""
    try:
        return await recommendation_service.get_recommendations(request)
    except Exception as e:
        logger.error(f"Error in recommendations endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Fraud Detection endpoints
@router.post("/detect-fraud", response_model=FraudDetectionResult)
async def detect_fraud(
    transaction: Transaction,
    fraud_detection_service: FraudDetectionService = Depends(get_fraud_detection_service)
):
    """Analyze a transaction for potential fraud."""
    try:
        return await fraud_detection_service.analyze_transaction(transaction)
    except Exception as e:
        logger.error(f"Error in fraud detection endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))