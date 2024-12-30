import subprocess
import os
import zipfile

cmd = "kaggle datasets download -d azathoth42/myanimelist -p ./anime_dataset"

try:
    print("Downloading dataset...")
    subprocess.run(cmd, check=True, shell=True)
    print("Dataset downloaded successfully!")
except subprocess.CalledProcessError as e:
    print("Error downloading the dataset:", e)


dataset_path="./anime_dataset/myanimelist.zip"
with zipfile.ZipFile(dataset_path, 'r') as zip_ref:
    zip_ref.extractall('./anime_dataset') 
    print("Done")

os.remove(dataset_path)
