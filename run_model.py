from fastapi import FastAPI
import joblib
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load('svd_book_recommendation_model.pkl')

# Define the input data model
class RatingRequest(BaseModel):
    user_id: str
    item_id: str
    
# Define the prediction route
@app.post('/predict')
def predict_rating(data: RatingRequest):
    # Make prediction
    prediction = model.predict(data.user_id, data.item_id).est
    return {'predicted_rating': prediction}
