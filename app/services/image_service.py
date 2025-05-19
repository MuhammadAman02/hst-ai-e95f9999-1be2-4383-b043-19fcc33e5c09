import io
import logging
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from typing import List, Tuple
import uuid
import os

logger = logging.getLogger(__name__)

class ImageService:
    def __init__(self):
        self.upload_folder = "app/static/uploads"
        os.makedirs(self.upload_folder, exist_ok=True)

    def save_image(self, image_data: bytes, filename: str) -> str:
        image_id = str(uuid.uuid4())
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{image_id}{file_extension}"
        file_path = os.path.join(self.upload_folder, new_filename)
        
        with open(file_path, "wb") as f:
            f.write(image_data)
        
        return image_id

    def analyze_skin_tone(self, image_data: bytes) -> Tuple[str, List[str]]:
        image = Image.open(io.BytesIO(image_data))
        image_array = np.array(image)
        
        # Reshape the image array to 2D
        pixels = image_array.reshape(-1, 3)
        
        # Use K-means clustering to find the dominant colors
        kmeans = KMeans(n_clusters=5)
        kmeans.fit(pixels)
        
        # Get the dominant color (assumed to be the skin tone)
        dominant_color = kmeans.cluster_centers_[0]
        
        # Convert RGB to hex
        skin_tone_hex = '#{:02x}{:02x}{:02x}'.format(int(dominant_color[0]), int(dominant_color[1]), int(dominant_color[2]))
        
        # Determine skin tone category (this is a simplified version)
        skin_tone_category = self.categorize_skin_tone(dominant_color)
        
        # Get recommended colors (this is a placeholder implementation)
        recommended_colors = self.get_recommended_colors(skin_tone_category)
        
        return skin_tone_category, recommended_colors

    def categorize_skin_tone(self, rgb_color: np.ndarray) -> str:
        # This is a simplified categorization. In a real application, you'd use a more sophisticated method.
        r, g, b = rgb_color
        luminance = 0.299 * r + 0.587 * g + 0.114 * b
        
        if luminance > 200:
            return "Light"
        elif luminance > 150:
            return "Medium"
        else:
            return "Dark"

    def get_recommended_colors(self, skin_tone: str) -> List[str]:
        # This is a placeholder. In a real application, you'd use a color theory algorithm or a pre-defined mapping.
        color_recommendations = {
            "Light": ["Navy", "Burgundy", "Forest Green", "Plum", "Charcoal"],
            "Medium": ["Coral", "Teal", "Olive", "Maroon", "Royal Blue"],
            "Dark": ["Gold", "Emerald", "Fuchsia", "Turquoise", "Tangerine"]
        }
        return color_recommendations.get(skin_tone, [])

    def modify_skin_tone(self, image_id: str, new_skin_tone: str) -> str:
        # This is a placeholder. Implementing realistic skin tone modification is complex and beyond the scope of this example.
        logger.warning("Skin tone modification is not implemented in this example.")
        return f"/static/uploads/{image_id}.jpg"  # Return the original image path