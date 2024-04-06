import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        # This method is triggered when a file or directory is created.
        if event.is_directory:
            print("Folder created.")
        else:
            print("File created.")

    def on_deleted(self, event):
        # This method is triggered when a file or directory is deleted.
        if event.is_directory:
            print("Folder deleted.")
        else:
            print("File deleted.")

class Watcher:
    DIRECTORY_TO_WATCH = "/Users/kevinwijaya/Desktop/Notes"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
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
