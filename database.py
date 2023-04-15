from dotenv import load_dotenv
from pymongo import MongoClient
import pymongo
import os

class databse:
    def __init__(self, mongo_client):
        load_dotenv()
        self.cluster = MongoClient(os.getenv(mongo_client))
        self.collection = self.cluster["Bugs"]["Dev"]

if __name__ == "__main__":
    pass