from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASS = os.environ.get("MONGO_PASS")
MONGO_CLUSTER_URL = os.environ.get("MONGO_CLUSTER_URL")

url = (f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_CLUSTER_URL}/?appName=COP4814")
client = MongoClient(url)
print(client)

print(client.list_database_names())

db1 = client.sample_mflix

print(db1.list_collection_names())

db2 = client["componentBased"] #db name
#since this db does not exist, it will be created

robot1 = db2["robot1"] #create a collection named robot1 for database componentBased

print(db2, robot1)

"""Example 1 -  Inserting 1 Document into Collection"""
datapoint1 = {"temp (f)": 87.2, "sal (ppt)": 60.2, "oxygen (mg/L)": 6.7}
result1 = robot1.insert_one(datapoint1)
print(result1)

"""Example 2 -  Inserting Many Document into Collection"""
datapoints= [{"temp (f)": 87.2, "sal (ppt)": 60.2, "oxygen (mg/L)": 6.7},
{"temp (f)": 28.4, "sal (ppt)": 35.2, "oxygen (mg/L)": 8.7},
{"temp (f)": 57.7, "sal (ppt)": 80.7, "oxygen (mg/L)": 6.1},
{"temp (f)": 82.4, "sal (ppt)": 64.8, "oxygen (mg/L)": 3.5},
{"temp (f)": 91.7, "sal (ppt)": 10.4, "oxygen (mg/L)": 3.0}]

result2 = robot1.insert_many(datapoints)
print(result2)

"""Example 3 - Query"""
#Find all documents where temperature is greater than 80
condition3 = {"temp (f)": {"$gt": 80}}
result3 = robot1.find(condition3)
for i in result3:
    print(i)

"""Example 4 -  Count number of docs that satisfy a certain condition"""
condition4 = {"sal (ppt)": {"$gt": 60}}
result4 = robot1.count_documents(condition4)
print(result4)

# Find the first movie
print("\n=== ONE MOVIE ===")
one = db1.movies.find_one()
print(one["title"])

# Find 5 movies from 2010
print("\n=== MOVIES FROM 2010 ===")
cursor = db1.movies.find({"year": 2010}).limit(5)
for m in cursor:
    print(m["title"])

# Find long movies (> 2h)
print("\n=== LONG MOVIES ===")
cursor = db1.movies.find({"runtime": {"$gt": 120}}, {"title": 1, "runtime": 1}).limit(5)
for m in cursor:
    print(m["title"], m["runtime"])

# Count how many movies from France
count = db1.movies.count_documents({"countries": "France"})
print("\nNumber of French movies:", count)