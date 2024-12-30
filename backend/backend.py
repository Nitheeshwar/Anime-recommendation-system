from fastapi import FastAPI
import reccomendation_functions as rf
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import matplotlib.pyplot as plt
import json
import requests
import string
import random

app = FastAPI()

anime_df=pd.read_csv("D:/Nitty/Personal Projects/Anime-recommendation-system/anime_dataset/Anime_Final.csv")



