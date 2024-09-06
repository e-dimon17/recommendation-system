# Recommendation System

This project demonstrates the use of a collaborative filtering recommendation system using the SVD algorithm on a book recommendation dataset. It includes model training, evaluation, and deployment using FastAPI.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Dataset](#dataset)
- [How to Run](#how-to-run)
- [Model Training](#model-training)
- [API Usage](#api-usage)

## Introduction

The project performs the following tasks:
- Downloads the book rating dataset from Kaggle.
- Preprocesses the data for use with the Surprise library.
- Trains an SVD model on the dataset.
- Evaluates the model using RMSE and cross-validation.
- Serves the trained model through a FastAPI application to predict ratings for specific user-item pairs.

## Requirements

Ensure you have the following dependencies installed:

```bash
fastapi
uvicorn
joblib
pandas
surprise
pyngrok
nest_asyncio
```

Install the required packages:

```bash
pip install fastapi uvicorn joblib pandas surprise pyngrok nest_asyncio
```

## Dataset

The dataset used in this project is the Book Recommendation Dataset, which you can download from Kaggle. Make sure to set up your Kaggle API credentials correctly to access the dataset.

## How to Run

1. **Download the dataset**:
   - The dataset will be automatically downloaded when you run `main.py`.

2. **Train the model**:
   - Run `main.py` to perform data preprocessing and model training.

   ```bash
   python main.py
   ```

   The trained SVD model will be saved as `svd_book_recommendation_model.pkl`.

3. **Start the FastAPI server**:
   - Run `run_model.py` to start the FastAPI server.

   ```bash
   python run_model.py
   ```

   The server will run and provide a public URL for accessing the API.

4. **Test the API**:
   You can use tools like Postman or `curl` to send POST requests to the API.

   Example `curl` request:

   ```bash
   curl -X POST "http://<public_url>/predict" -H "Content-Type: application/json" -d '{
     "user_id": "12345",
     "item_id": "978-3-16-148410-0"
   }'
   ```

   The response will return the predicted rating for the specified user and item.

## Model Training

The `main.py` script performs the following:

1. Downloads the Book Recommendation dataset from Kaggle.
2. Loads the dataset and displays the first few rows.
3. Prepares the data for the Surprise library.
4. Trains an SVD model on the dataset and evaluates its performance using RMSE and cross-validation.
5. Saves the trained model to a file (`svd_book_recommendation_model.pkl`).

## API Usage

The `run_model.py` script uses FastAPI to serve predictions based on the trained model. You can send data in the following format:

```json
{
  "user_id": "12345",
  "item_id": "978-3-16-148410-0"
}
```

The response will provide the predicted rating for the specified user-item pair.
