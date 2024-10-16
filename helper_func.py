import pymongo
from config import DB_URI, DB_NAME

# Initialize MongoDB client and database
dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

# Collections
user_data = database['users']  # For general user data
req_one = database['req_one']  # Requests for Channel 1
req_two = database['req_two']  # Requests for Channel 2
req_three = database['req_three']  # Requests for Channel 3


# Function to check if a user is already in the main user_data collection
async def present_user(user_id: int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)


# Function to add a new user to the main user_data collection
async def add_user(user_id: int):
    if not present_user(user_id):  # Avoid duplicate entries
        user_data.insert_one({'_id': user_id})


# Function to get all users from the main user_data collection
async def full_userbase():
    user_docs = user_data.find()
    user_ids = [doc['_id'] for doc in user_docs]  # Use list comprehension for cleaner code
    return user_ids


# Function to delete a user from the main user_data collection
async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})


# Function to check if a user has requested to join Channel 1
async def is_requested_one(user_id: int):
    user = req_one.find_one({"user_id": user_id})
    return bool(user)


# Function to check if a user has requested to join Channel 2
async def is_requested_two(user_id: int):
    user = req_two.find_one({"user_id": user_id})
    return bool(user)


# Function to check if a user has requested to join Channel 3
async def is_requested_three(user_id: int):
    user = req_three.find_one({"user_id": user_id})
    return bool(user)


# Function to add a request for Channel 1
async def add_req_one(user_id: int):
    if not is_requested_one(user_id):  # Avoid duplicate requests
        req_one.insert_one({"user_id": user_id})


# Function to add a request for Channel 2
async def add_req_two(user_id: int):
    if not is_requested_two(user_id):  # Avoid duplicate requests
        req_two.insert_one({"user_id": user_id})


# Function to add a request for Channel 3
async def add_req_three(user_id: int):
    if not is_requested_three(user_id):  # Avoid duplicate requests
        req_three.insert_one({"user_id": user_id})


# Function to remove all requests from Channel 1 (for cleanup purposes)
async def delete_all_one():
    req_one.delete_many({})


# Function to remove all requests from Channel 2 (for cleanup purposes)
async def delete_all_two():
    req_two.delete_many({})


# Function to remove all requests from Channel 3 (for cleanup purposes)
async def delete_all_three():
    req_three.delete_many({})
    
