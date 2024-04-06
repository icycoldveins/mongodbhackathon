import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pymongo
import requests
from nomic import embed
import os
import numpy as np
import uuid

# Connect to your Atlas cluster
client = pymongo.MongoClient("connection string")# Replace 'your_database_name' with the name of your database
db = client.your_database_name
# Replace 'your_collection_name' with the name of your collection
collection = db.your_collection_name


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        # This method is triggered when a file or directory is created.
        if event.is_directory:
            print("Folder created.")
        else:
            if event.src_path.endswith('.txt'):
                print(f"Text file created: {event.src_path}")
                file_uuid = uuid.uuid4()
                print(f"Generated UUID for {event.src_path}: {file_uuid}")

                try:
                    # Attempt to read the contents of the created text file
                    with open(event.src_path, 'r') as file:
                        data = file.read()
                        # Assuming embed.text() works as expected and no exceptions are raised
                        output = embed.text(
                            texts=[data],
                            model='nomic-embed-text-v1.5',
                            task_type='search_document'
                        )
                        embeddings = np.array(output['embeddings'])
                        # Print the shape or size of embeddings to confirm successful creation
                        print(
                            f"Embeddings created with shape: {embeddings.shape}")
                except Exception as e:
                    print(f"An error occurred while processing the file: {e}")
            else:
                print(f"Ignoring non-text file: {event.src_path}")

    def on_deleted(self, event):
        # This method is triggered when a file or directory is deleted.
        if event.is_directory:
            print("Folder deleted.")
        else:
            print("File deleted:", event.src_path)
            # Retrieve and delete the document using the file path
            try:
                # Find the document using the file path
                document = collection.find_one({"file_path": event.src_path})
                if document:
                    # Print the found UUID (for confirmation)
                    print(
                        f"Found UUID for {event.src_path}: {document['uuid']}")

                    # Delete the document from the database
                    collection.delete_one({"file_path": event.src_path})
                    print(
                        f"Deleted document for {event.src_path} from the database.")
                else:
                    print(f"No document found for {event.src_path}.")
            except Exception as e:
                print(
                    f"An error occurred while deleting the file from the database: {e}")

# Ensure you replace 'your_mongodb_connection_string', 'your_database_name', and 'your_collection_name'
# with the actual values from your MongoDB Atlas setup.


class Watcher:
    DIRECTORY_TO_WATCH = "/Users/kevinwijaya/Desktop/Notes"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(3)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer Stopped")
        self.observer.join()


if __name__ == "__main__":
    w = Watcher()
    w.run()
