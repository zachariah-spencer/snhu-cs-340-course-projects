# crud_module.py

from pymongo import MongoClient
from pymongo.errors import PyMongoError

class CRUD:
    def __init__(self, user, pw):
        """
        Initialize the MongoDB client and set up the database and collection.
        Connection variables are hard-coded for the 'aacuser' account.
        """
        
        self.user = user
        self.pw = pw
        
        # Connection Variables (modify as needed)
        USER = self.user
        PASS = self.pw
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34139
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize the MongoDB client using the connection string
        connection_str = f'mongodb://{USER}:{PASS}@{HOST}:{PORT}'
        self.client = MongoClient(connection_str)
        
        # Set the target database and collection
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        if data is None or not isinstance(data, dict):
            raise ValueError("Data must be a non-empty dictionary.")
        
        try:
            result = self.collection.insert_one(data)
            # The insert_one result includes an 'acknowledged' property indicating success.
            return result.acknowledged
        except PyMongoError as e:
            # Log error information if needed (here we simply return False)
            print(f"Insert Error: {e}")
            return False

    def read(self, query):
        if query is None or not isinstance(query, dict):
            raise ValueError("Query must be a dictionary.")
        
        try:
            # Use find() to return a cursor and convert it to a list.
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            # Log error information if needed (here we simply return an empty list)
            # print(f"Query Error: {e}")
            return []

    def update(self, query, update_values, many=True):
        if query is None or not isinstance(query, dict):
            raise ValueError("Query must be a dictionary.")
        if update_values is None or not isinstance(update_values, dict):
            raise ValueError("Update values must be a dictionary.")

        try:
            if many:
                result = self.collection.update_many(query, update_values)
            else:
                result = self.collection.update_one(query, update_values)
            return result.modified_count
        except PyMongoError as e:
            print(f"Update Error: {e}")
            return 0

    def delete(self, query, many=True):
        if query is None or not isinstance(query, dict):
            raise ValueError("Query must be a dictionary.")
        
        try:
            if many:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete Error: {e}")
            return 0
