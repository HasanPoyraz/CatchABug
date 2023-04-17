from dotenv import load_dotenv
from pymongo import MongoClient
import pymongo
import os

class database: # unfinashed
    def __init__(self, mongo_client):
        load_dotenv()
        self.cluster = MongoClient(os.getenv(mongo_client))
        self.collection = self.cluster["Bugs"]["Dev"]

    def new_entry(self, title, error, text):
        try:
            id = self.collection.find_one(sort=[("_id", pymongo.DESCENDING)])["_id"]
            _id = id + 1
        except TypeError:
            _id = 0

        post = {"_id": _id, "title": title, "error": error, "text": text, "fixed": 0}

        self.collection.insert_one(post)

        print("Sucsesfully inserted post:\n", post, "\n")

    def list_entry(self, atb=None):
        x = 0
        if atb == None:
            for doc in self.collection.find({"fixed": 0}):
                x += 1
                print(doc["_id"], "-->", doc["title"])

            if x == 0:
                print("No entries found.")

        elif atb == "a":
            for doc in self.collection.find():
                x += 1

                if doc["fixed"] == 1:
                    print(doc["_id"], "- fixed -->", doc["title"])
                else:
                    print(doc["_id"], "-->", doc["title"])

            if x == 0:
                print("No entries found.")

        elif atb == "f":
            for doc in self.collection.find({"fixed": 1}):
                x += 1
                print(doc["_id"], "-->", doc["title"])

            if x == 0:
                print("No fixed entries found.")

    def display_entry(self, id):
        entry = self.collection.find_one({"_id": id})
        print(f"""[Id] --> {entry["_id"]}""")
        print(f"""[Title] --> {entry["title"]}""")
        print(f"""[Error] --> {entry["error"]}""")
        print(f"""[Text] --> {entry["text"]}""")
        print(f"""[Fixed] --> {entry["fixed"]}""")

    def mark_entry(self, id):
        entry = self.collection.find_one({"_id": id})
        entry["fixed"] = 1
        self.collection.update_one({"_id": id}, {"$set": entry})

        print(f"Entry with the id {id} marked as fixed.")

if __name__ == "__main__":
    pass