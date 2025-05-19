from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid

# Chatbot Models
class Message(BaseModel):
    """Represents a single message in a conversation."""
    content: str
    role: str = "user"  # "user" or "assistant"
    timestamp: datetime = Field(default_factory=datetime.now)

class Conversation(BaseModel):
    """Represents a conversation with multiple messages."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    messages: List[Message] = []
    metadata: Optional[Dict[str, Any]] = None

# NLP Models
class TextAnalysisRequest(BaseModel):
    """Request model for text analysis operations."""
    text: str
    analysis_type: str  # "sentiment", "entities", "classification", etc.
    options: Optional[Dict[str, Any]] = None

class TextAnalysisResponse(BaseModel):
    """Response model for text analysis operations."""
    result: Dict[str, Any]
    processing_time: float
    model_used: str

# Recommendation System Models
class RecommendationRequest(BaseModel):
    """Request model for recommendation operations."""
    user_id: str
    item_context: Optional[Dict[str, Any]] = None
    num_recommendations: int = 5
    filters: Optional[Dict[str, Any]] = None

class RecommendationItem(BaseModel):
    """Represents a single recommended item."""
    item_id: str
    score: float
    metadata: Optional[Dict[str, Any]] = None

class RecommendationResponse(BaseModel):
    """Response model for recommendation operations."""
    recommendations: List[RecommendationItem]
    user_id: str
    processing_time: float
    model_used: str

# Fraud Detection Models
class TransactionStatus(str):
    PENDING = "pending"
    COMPLETED = "completed"
    REJECTED = "rejected"
    FLAGGED = "flagged"

class Transaction(BaseModel):
    """Represents a transaction for fraud detection."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    amount: float
    timestamp: datetime = Field(default_factory=datetime.now)
    user_id: str
    merchant: str
    location: Optional[str] = None
    device_info: Optional[Dict[str, Any]] = None
    status: str = TransactionStatus.PENDING

class FraudDetectionResult(BaseModel):
    """Result of fraud detection analysis."""
    transaction_id: str
    risk_score: float  # 0-1 where 1 is highest risk
    is_fraudulent: bool
    confidence: float
    reasons: List[str] = []
    model_used: str