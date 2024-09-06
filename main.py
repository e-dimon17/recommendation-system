import subprocess
import pandas as pd

# Define the Kaggle dataset URL and filename
kaggle_url = "arashnic/book-recommendation-dataset"
file_name = "data/Ratings.csv"

# Use Kaggle API to download the file
subprocess.run(['kaggle', 'datasets', 'download', '-d', kaggle_url, '-f', file_name])

# Unzip the downloaded file
subprocess.run(['unzip', f'{file_name}.zip'])

# Load the dataset
ratings = pd.read_csv(file_name)

# Display the first few rows
ratings.head()

from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate

# Load data into Scikit-surprise format
reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(ratings[['User-ID', 'ISBN', 'Book-Rating']], reader)

# Test the trained algorithm
from surprise import accuracy
from surprise.model_selection import train_test_split

# Use SVD algorithm
model = SVD()

# Train-test split
trainset, testset = train_test_split(data, test_size=0.2)
model.fit(trainset)
predictions = model.test(testset)

# Calculate RMSE
accuracy.rmse(predictions)
