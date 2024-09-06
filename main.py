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