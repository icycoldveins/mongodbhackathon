from nomic import embed
import pymongo
from typing import List
import time
import os
import sys
from bson.objectid import ObjectId




MONGO_URI = (
    "mongodb+srv://princegeutler:rfVtYK0uUq4tLTpY@cluster0.tpnl2sp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

try: 
        client = pymongo.MongoClient(MONGO_URI)
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client.myDatabase

def generate_embeddings(input_texts: List[str], model_api_string: str, task_type="search_document") -> List[List[float]]:
        """Generate embeddings from Nomic Embedding API
        Args:
                input_texts: a list of string input tects. 
                model_api_string: str. An API string for a specific embedding model of your choice.
                tast_type: str. the task type for the embedding model. Defaults to "search_document". One of 'search_query', 'search_document', 'classification', or 'clustering', we probably want to use clustering
        Returns: 
                a list of embeddings. Each element corresponds to each input text.
        
        """
        start = time.time()
        outputs = embed.text(
                texts = [f"{text}" for text in input_texts],
                model = model_api_string,
                task_type = task_type,
        )
        print(f"Embedding generation took {str(time.time() - start)} seconds")
        return outputs["embeddings"]



def insertDocumentEmbedding(document: str, uuid: ObjectId):
        embedding_model_string = 'nomic-embed-text-v1'
        vector_database_field_name = 'nomic-embed-text'
        NUM_DOC_LIMIT = 250 
        sample_output = generate_embeddings([document], embedding_model_string)
        doc = {}
        doc[vector_database_field_name] = generate_embeddings([document], embedding_model_string)
    
        try:
                db["documents"].replace_one({'_id': uuid}, doc)      
        except pymongo.errors.OperationFailure:
                print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
                sys.exit(1)

def insertFolderEmbedding(folder: str, uuid: ObjectId):
      db["folders"].insert_one({"_id": uuid, "embedding": folder})
      
          

    



