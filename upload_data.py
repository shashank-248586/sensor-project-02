from pymongo.mongo_client import MongoClient
import pandas as pd
import json
url = r"mongodb+srv://shashankshekhartripathy36:suman@cluster0.vdynv9m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
clint = MongoClient(url)
DATABASE_NAME = "pwskils"
COLLECTION_NAME = 'waferfalt'
data = pd.read_csv(r"C:\Users\suman\Desktop\SENSORP\notebooks\wafer_23012020_041211.csv")
data.drop(columns=["Unnamed: 0"],inplace=True)
json_record = list(json.loads(data.T.to_json()).values())
clint[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)